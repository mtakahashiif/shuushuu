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
}


class ApiBuilder基本コンソールの機器一覧(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100000303', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'HW機器種別': 'SV',
                'ホスト名': params['hostname'],
                'IPアドレス': params['ip_address'],
                'ログインユーザID': params['login_username'],
                'ログインパスワード/管理': '●',
                'ログインパスワード/ログインパスワード': params['login_password'],
                'Ansible利用情報/Legacy/Role利用情報/認証方式': 'パスワード認証',
                'Ansible利用情報/Tower利用情報/接続タイプ': 'machine'
            }
        ]

class ApiBuilder基本コンソールのオペレーション一覧(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100000304', 'EDIT')


    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'オペレーション名': params['operation_name'],
                '実施予定日時': params['scheduled_date'],
            }
        ]


api_invoker = ita.ApiInvoker(ita.ApiContext())
api_invoker.invoke(params, ApiBuilder基本コンソールの機器一覧())
api_invoker.invoke(params, ApiBuilder基本コンソールのオペレーション一覧())
