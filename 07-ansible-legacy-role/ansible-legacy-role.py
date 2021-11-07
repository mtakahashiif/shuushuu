import os
import exastro_api.ita.v1 as ita

from typing import *


params = {
    'hostname': 'target',
    'ip_address': '0.0.0.0',     # dummy
    'login_username': 'root',
    'login_password': 'hogehoge',

    'operation_name': 'テストoperation',
    'scheduled_date': '2021/10/30 20:17',

    'menu_name': 'テスト用メニュー',

    'movement_name': 'テストmovement',
    'header_section': '''
- hosts: all
  remote_user: "{{ __loginuser__ }}"
  gather_facts: yes
  become: yes
'''[1:-1],

    'role_package_name': 'テスト用収集ロール',
    'upload_file': os.path.join(os.environ['WORKSPACE_DIR'], 'upload-file.zip'),
    'role_package_include_order': '1',
    'role_name': 'data_collector',
}


class ApiBuilderAnsibleLegacyRoleのMovement一覧(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020306', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'Movement名': params['movement_name'],
                'Ansible利用情報/ホスト指定形式': 'ホスト名',
                'Ansible利用情報/ヘッダーセクション': params['header_section']
            }
        ]


class ApiBuilderAnsibleLegacyRoleのロールパッケージ管理(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020303', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'ロールパッケージ名': params['role_package_name'],
                'ロールパッケージファイル(ZIP形式)': ita.UploadFile(params['upload_file'])
            }
        ]


class ApiBuilderAnsibleLegacyRoleのMovementロール紐付(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020307', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                "Movement": ita.Query('2100020306', '$[?(@."Movement名"="{}")]."MovementID","Movement名"'.format(params['movement_name'])),
                "ロールパッケージ名：ロール名": ita.Join([
                    ita.Query('2100020303', '$[?(@."ロールパッケージ名"="{}")]."項番","ロールパッケージ名"'.format(params['role_package_name'])),
                    ita.Query('2100020304', '$[?(@."ロールパッケージ名"="{}" & @."ロール名"="{}")]."項番","ロール名"'.format(params['role_package_name'], params['role_name']))
                ]),
                "インクルード順序": params['role_package_include_order']
            }
        ]

api_invoker = ita.ApiInvoker(ita.ApiContext())
api_invoker.invoke(params, ApiBuilderAnsibleLegacyRoleのMovement一覧())
api_invoker.invoke(params, ApiBuilderAnsibleLegacyRoleのロールパッケージ管理())
api_invoker.invoke(params, ApiBuilderAnsibleLegacyRoleのMovementロール紐付())
