import base64
import json
import os.path
import time
import urllib.request
import urllib.response

from abc import abstractmethod


def sort_dict_by_key_as_int(src):
    return dict(sorted(src.items(), key=lambda item: int(item[0])))


class ApiContext:
    def __init__(self):
        self.protocol = os.environ.get('EXASTRO_PROTOCOL')
        self.host = os.environ.get('EXASTRO_HOST')
        self.port = os.environ.get('EXASTRO_PORT')
        self.username = os.environ.get('EXASTRO_USERNAME')
        self.password = os.environ.get('EXASTRO_PASSWORD')
        self.workspace = os.environ.get('WORKSPACE_DIR')
        self.debug = bool(os.environ.get('DEBUG'))

    def createApiRequest(self, menu_id):
        return ApiRequest(
            urllib.parse.urlunparse((
                self.protocol,
                self.host + ':' + self.port,
                '/default/menu/07_rest_api_ver1.php',
                '',
                urllib.parse.urlencode({'no': menu_id}),
                ''
            )),
            self.username,
            self.password
        )

    def get_workspace_path(self, relative_path):
        return os.path.join(self.workspace, relative_path)


class ApiRequest:
    def __init__(self, url, username, password):
        self.url = url
        self.credential = base64.b64encode((username + ':' + password).encode()).decode()

    def invoke(self, command, data=None):

        print(self.url)
        method = "POST"
        headers = {'Content-Type': 'application/json', 'Authorization': self.credential, 'X-Command': command}
        request = urllib.request.Request(self.url, method=method, headers=headers, data=data.encode())   # urllib.request.Request

        return ApiResponse(
            urllib.request.urlopen(request)
        )


class ApiResponse:
    def __init__(self, response):
        self.response = response    # http.client.HTTPResponse

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.response.isclosed():
            self.response.close()
    
    def get_status(self):
        return self.response.status

    def get_body(self):
        return self.response.read()


class UploadFile:
    def __init__(self, file_path):
        self.file_name = os.path.basename(file_path)
        self.file_path = file_path

    def get_base64(self):
        with open(self.file_path, "rb") as file:
            return base64.b64encode(file.read()).decode("ascii")


class ColumnMetadataFinder:
    @abstractmethod
    def find(self, id):
        pass


column_metadata_finder = ColumnMetadataFinder()


class ColumnMetadata:
    def __init__(self, menu_id, column_names, file_upload_column_names):
        self.menu_id = menu_id
        self.column_names = column_names
        self.file_upload_column_names = file_upload_column_names


class ApiBuilderError(Exception):
    pass


class ApiBuilder:
    column_metadata_finder = None

    def __init__(self, menu_id, command):
        self.menu_id = menu_id
        self.column_metadata = ApiBuilder.column_metadata_finder.find(menu_id)
        self.command = command
        self.entries = []


    def __validate(self, entry):
        for column_name in entry.keys():
            if not column_name in self.column_metadata.column_names:
                raise ApiBuilderError('Invalid column name "{}"'.format(column_name))

        mandatory_column_names = ['実行処理種別']
        for column_name in mandatory_column_names:
            if not column_name in entry.keys():
                raise ApiBuilderError('Mandatory item "{}" not contained'.format(column_name))

        verb = entry['実行処理種別']
        if not verb in ['登録', '更新', '廃止', '復活']:
            raise ApiBuilderError('Invalid verb {}'.format(verb))


    @abstractmethod
    def build(self, params):
        pass


    def add_entry(self, entry):
        self.__validate(entry)
        self.entries.append(entry)


    def __convert_to_element_key(self, column_name):
        return str(self.column_metadata.column_names.index(column_name))


    def __convert_to_element_value(self, value):
        if isinstance(value, UploadFile):
            result = value.file_name
        elif isinstance(value, bool):
            result = "true" if value else "false"
        else:
            result = str(value)

        return result


    def __convert_to_entry_key(self, index):
        return str(index)


    def __convert_to_entry_value(self, entry):
        result = {}

        for column_name, value in entry.items():
            element_key = self.__convert_to_element_key(column_name)
            element_value = self.__convert_to_element_value(value)
            result[element_key] = element_value

        return sort_dict_by_key_as_int(result)


    def __convert_to_upload_file(self):
        upload_file_json_object = []

        for entry in self.entries:
            upload_file_entry_json_object = {}

            for file_upload_column_name in self.column_metadata.file_upload_column_names:
                if file_upload_column_name in entry.keys():
                    key = int(self.column_metadata.column_names.index(file_upload_column_name))
                    value = entry[file_upload_column_name].get_base64()
                    upload_file_entry_json_object[key] = value

            upload_file_json_object.append(sort_dict_by_key_as_int(upload_file_entry_json_object))
        
        return upload_file_json_object


    def to_json_object(self):
        json_object = {}

        for entry_index, entry in enumerate(self.entries):
            entry_key = self.__convert_to_entry_key(entry_index)
            entry_value = self.__convert_to_entry_value(entry)
            json_object[entry_key] = entry_value

        if self.column_metadata.file_upload_column_names:
            json_object['UPLOAD_FILE'] = self.__convert_to_upload_file()

        return json_object


class ApiInvoker:
    def __init__(self, api_context):
        self.api_context = api_context
        self.builders = []

        # cut the last 4 digits of integer part of UNIX time
        self.debug_file_dir = 'debug-{}'.format(time.time())
    
    def add_builder(self, builder):
        self.builders.append(builder)

    def invoke(self, params):
        for index, builder in enumerate(self.builders):
            # create request
            request = self.api_context.createApiRequest(builder.menu_id)

            # DEBUG: save API URL
            if self.api_context.debug:
                self.__save_to_file(index, 'api-url', builder, 'txt', request.url)

            # create JSON
            builder.build(params)
            request_body = json.dumps(builder.to_json_object())

            # DEBUG: save request JSON
            if self.api_context.debug:
                self.__save_to_file(index, 'request', builder, 'json', request_body)

            # invoke API
            with request.invoke(builder.command, request_body) as response:
                response_body = response.get_body().decode()

            # DEBUG: save response JSON
            if self.api_context.debug:
                self.__save_to_file(index, 'response', builder, 'json', response_body)

    def __save_to_file(self, index, kind, builder, ext, data):
        dir_path = self.api_context.get_workspace_path(self.debug_file_dir)
        os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, "{:03}-{}-{}.{}".format(index, kind, type(builder).__name__, ext))
        with open(file_path, mode='w') as f:
            f.write(data)



class SimpleIndexCounter:
    def __init__(self, begin=0, step=1):
        self.value = begin
        self.step = step

    def __call__(self):
        value = self.value
        self.value += 1
        return value
