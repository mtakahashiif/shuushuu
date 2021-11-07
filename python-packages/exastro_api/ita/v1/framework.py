import base64
import functools
import http.client
import json
import os.path
import time
import urllib.parse
import urllib.request
import urllib.response

from abc import abstractmethod, ABC
from jsonpath_ng.ext import parse
from typing import *


def sort_dict_by_key_as_int(src: dict):
    return dict(sorted(src.items(), key=lambda item: int(item[0])))


class ApiResponse:
    def __init__(self, response: http.client.HTTPResponse):
        self.response: http.client.HTTPResponse = response

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.response.isclosed():
            self.response.close()
    
    def get_status(self):
        return self.response.status

    def get_body(self):
        return self.response.read()


class ApiRequest:
    def __init__(self, url: str, username: str, password: str) -> None:
        self.url: str = url
        self.credential: str = base64.b64encode((username + ':' + password).encode()).decode()

    def invoke(self, command: str, data: str = None) -> ApiResponse:
        method = "POST"
        headers = {'Content-Type': 'application/json', 'Authorization': self.credential, 'X-Command': command}
        request = urllib.request.Request(
            self.url,
            method = method,
            headers = headers,
            data = data.encode() if data is not None else None
        )

        return ApiResponse(
            urllib.request.urlopen(request)
        )


class ApiContext:
    def __init__(self) -> None:
        self.protocol: str = os.getenv('EXASTRO_PROTOCOL', 'http')
        self.host: str = os.environ.get('EXASTRO_HOST', 'localhost')
        self.port: str = os.environ.get('EXASTRO_PORT', '8080')
        self.username: str = os.environ.get('EXASTRO_USERNAME', 'administrator')
        self.password: str = os.environ.get('EXASTRO_PASSWORD', 'password')
        self.workspace: str = os.environ.get('WORKSPACE_DIR', 'tmp')
        self.debug: bool = bool(os.environ.get('DEBUG'))

    def create_api_request(self, menu_id: str) -> ApiRequest:
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

    def get_workspace_path(self, relative_path: str) -> str:
        return os.path.join(self.workspace, relative_path)


class ItemValue(ABC):
    @abstractmethod
    def to_value(self, api_context: ApiContext) -> str:
        pass


class UploadFile(ItemValue):
    def __init__(self, file_path: str) -> None:
        self.file_name: str = os.path.basename(file_path)
        self.file_path: str = file_path


    def to_value(self, api_context: ApiContext) -> str:
        return self.file_name


    def get_base64(self) -> str:
        with open(self.file_path, "rb") as file:
            return base64.b64encode(file.read()).decode("ascii")


class ColumnMetadata:
    def __init__(self, menu_id: str, column_names: List[str], file_upload_column_names: List[str]) -> None:
        self.menu_id: str = menu_id
        self.column_names: List[str] = column_names
        self.file_upload_column_names: List[str] = file_upload_column_names


class ColumnMetadataFinder(ABC):
    @abstractmethod
    def find(self, menu_id: str) -> ColumnMetadata:
        pass


class ApiBuilderError(Exception):
    pass


class ApiBuilder:
    column_metadata_finder: ClassVar[ColumnMetadataFinder]

    def __init__(self, menu_id: str, command: str) -> None:
        self.menu_id: str = menu_id
        self.command: str = command
        self.column_metadata: ColumnMetadata = ApiBuilder.column_metadata_finder.find(menu_id)


    @abstractmethod
    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        pass


    def __validate_entries(self, entries: List[Dict[str, str]]) -> None:
        for entry in entries:
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


    def __convert_to_item_key(self, column_name: str) -> str:
        return str(self.column_metadata.column_names.index(column_name))


    def __convert_to_item_value(self, api_context: ApiContext, value: Any) -> str:
        if isinstance(value, ItemValue):
            result = value.to_value(api_context)
        elif isinstance(value, bool):
            result = "true" if value else "false"
        else:
            result = str(value)

        return result


    def __convert_to_entry_key(self, index: int) -> str:
        return str(index)


    def __convert_to_entry_value(self, api_context: ApiContext, entry: Dict[str, Any]) -> Dict[str, str]:
        result = {}

        for column_name, value in entry.items():
            element_key = self.__convert_to_item_key(column_name)
            element_value = self.__convert_to_item_value(api_context, value)
            result[element_key] = element_value

        return sort_dict_by_key_as_int(result)


    def __convert_to_upload_file(self, entries: List[Dict[str, str]]) -> List[Dict[str, str]]:
        upload_file_json_object = []

        for entry in entries:
            upload_file_entry_json_object = {}

            for file_upload_column_name in self.column_metadata.file_upload_column_names:
                if file_upload_column_name in entry.keys():
                    key = int(self.column_metadata.column_names.index(file_upload_column_name))

                    x = entry[file_upload_column_name]
                    if isinstance(x, UploadFile):
                        value = x.get_base64()
                    else:
                        raise ApiBuilderError('The value type "{}" is invalid for upload file column'.format(type(x).__name__))

                    upload_file_entry_json_object[key] = value

            upload_file_json_object.append(sort_dict_by_key_as_int(upload_file_entry_json_object))
        
        return upload_file_json_object


    def create_json_object(self, api_context: ApiContext, params: Dict[str, str]) -> Optional[Dict[str, Any]]:
        json_object: Optional[Dict[str, Any]] = None

        entries = self.create_entries(params)
        if entries is not None:
            self.__validate_entries(entries)

            json_object = {}
            for entry_index, entry in enumerate(entries):
                entry_key = self.__convert_to_entry_key(entry_index)
                entry_value = self.__convert_to_entry_value(api_context, entry)
                json_object[entry_key] = entry_value

            if self.column_metadata.file_upload_column_names:
                json_object['UPLOAD_FILE'] = self.__convert_to_upload_file(entries)

        return json_object


class Join(ItemValue):
    def __init__(self, item_values: List[ItemValue], separator: str = ':') -> None:
        self.separator: str = separator
        self.item_values: List[ItemValue] = item_values


    def to_value(self, api_context: ApiContext) -> str:
        return functools.reduce(lambda x, y: x + self.separator + y, map(lambda x: x.to_value(api_context), self.item_values))


class Query(ItemValue):
    def __init__(self, menu_id: str, query_string: str, separator: str = ':') -> None:
        self.menu_id: str = menu_id
        self.query_string: str = query_string
        self.separator = separator


    def to_value(self, api_context: ApiContext) -> str:
        class ApiBuilderFilter(ApiBuilder):
            def __init__(self, menu_id: str) -> None:
                super().__init__(menu_id, 'FILTER')
        
            def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
                return None

        api_invoker = ApiInvoker(api_context)
        response_json = api_invoker.invoke(dict(), ApiBuilderFilter(self.menu_id))

        data_object = json.loads(response_json)

        # convert API response to process JSONPath
        #
        # ***** BEFORE *****
        #     {
        #       "status": "SUCCEED",
        #       "resultdata": {
        #         "CONTENTS": {
        #           "RECORD_LENGTH": 1,
        #           "BODY": [
        #             [
        #               "key0",
        #               "key1",
        #               "key2",
        #               ...
        #             ],
        #             [
        #               "value0",
        #               "value1",
        #               "value2",
        #               ...
        #             ],
        #             ...
        #             
        # ***** AFTER *****
        #      
        #     [
        #       {
        #         key0: value0
        #         key1: value1
        #         key2: value2
        #         ...
        #       },
        #       {
        #         key0: value0
        #         key1: value1
        #         key2: value2
        #         ...
        #       }, 
        #       ...
        converted = []
        keys = data_object['resultdata']['CONTENTS']['BODY'][0]
        for entry in data_object['resultdata']['CONTENTS']['BODY'][1:]:
            converted_entry = {}
            for index in range(len(keys)):
                converted_entry[keys[index]] = entry[index]

            converted.append(converted_entry)

        jsonpath_expr = parse(self.query_string)
        matches = jsonpath_expr.find(converted)
        values = [match.value for match in matches]

        return functools.reduce(lambda x, y: x + self.separator + y, values)


class ApiInvokerError(Exception):
    pass


class ApiInvoker:
    def __init__(self, api_context: ApiContext) -> None:
        self.api_context: ApiContext = api_context
        self.debug_file_dir = 'debug-{}'.format(time.time())


    def invoke(self, params: Dict[str, str], builder: ApiBuilder) -> str:
        request = self.api_context.create_api_request(builder.menu_id)

        # DEBUG: save API URL
        if self.api_context.debug:
            self.__save_to_file(0, 'api-url', builder, 'txt', request.url)

        # create JSON
        request_body = json.dumps(builder.create_json_object(self.api_context, params))

        # DEBUG: save request JSON
        if self.api_context.debug:
            self.__save_to_file(1, 'request', builder, 'json', request_body)

        # invoke API
        with request.invoke(builder.command, request_body) as response:
            response_body = response.get_body().decode()

        # DEBUG: save response JSON
        if self.api_context.debug:
            self.__save_to_file(2, 'response', builder, 'json', response_body)

        return response_body


    def __save_to_file(self, index: int, kind: str, builder: ApiBuilder, file_ext: str, data: str) -> None:
        dir_path = self.api_context.get_workspace_path(self.debug_file_dir)
        os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, "{:03}-{}-{}.{}".format(index, kind, type(builder).__name__, file_ext))
        with open(file_path, mode='w') as f:
            f.write(data)


class SimpleIndexCounter:
    def __init__(self, begin: int = 0, step: int = 1) -> None:
        self.value: int = begin
        self.step: int = step


    def __call__(self) -> int:
        value = self.value
        self.value += 1
        return value
