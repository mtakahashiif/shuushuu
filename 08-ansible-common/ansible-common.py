import exastro_api.ita.v1 as ita
import os

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

    'shuushuu_file_prefix': 'collected-data'
}


class ApiBuilderAnsible共通の収集項目値管理(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100040710', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                '収集項目(FROM)/パース形式': 'YAML',
                '収集項目(FROM)/PREFIX(ファイル名)': params['shuushuu_file_prefix'],
                '収集項目(FROM)/変数名': '',
            }
        ]

api_invoker = ita.ApiInvoker(ita.ApiContext())
api_invoker.invoke(params, ApiBuilderAnsible共通の収集項目値管理())
