import os
import exastro_api.ita.v1 as ita


class Params:
    def __init__(self):
        self.hostname = 'target'
        self.ip_address = '0.0.0.0'     # dummy
        self.login_username = 'root'
        self.login_password = 'hogehoge'

        self.operation_name = 'テストoperation'
        self.scheduled_date = '2021/10/30 20:17'

        self.movement_name = "テストmovement"
        self.header_section = '''
- hosts: all
  remote_user: "{{ __loginuser__ }}"
  gather_facts: yes
  become: yes
'''[1:-1]

        self.role_package_name = 'テスト用収集ロール'
        self.upload_file = ita.UploadFile(os.path.join(os.environ['WORKSPACE_DIR'], 'upload-file.zip'))


#Movement一覧
#ロールパッケージ管理
#Movement-ロール紐付

class ApiBuilderAnsibleLegacyRoleのMovement一覧(ita.ApiBuilder):
    def __init__(self):
        super().__init__('2100020306', 'EDIT')

    def build(self, params):
        self.add_entry({
            '実行処理種別': '登録',
            'Movement名': params.movement_name,
            'Ansible利用情報/ホスト指定形式': 'ホスト名',
            'Ansible利用情報/ヘッダーセクション': params.header_section
        })


class ApiBuilderAnsibleLegacyRoleのロールパッケージ管理(ita.ApiBuilder):
    def __init__(self):
        super().__init__('2100020303', 'EDIT')

    def build(self, params):
        self.add_entry({
            '実行処理種別': '登録',
            'ロールパッケージ名': params.role_package_name,
            'ロールパッケージファイル(ZIP形式)': params.upload_file
        })


api_invoker = ita.ApiInvoker(ita.ApiContext())
api_invoker.add_builder(ApiBuilderAnsibleLegacyRoleのMovement一覧())
api_invoker.add_builder(ApiBuilderAnsibleLegacyRoleのロールパッケージ管理())
api_invoker.invoke(Params())
