import exastro_api.ita.v1 as ita

from typing import *


params = {
    'hostname': 'target',
    'ip_address': '0.0.0.0',     # dummy
    'login_username': 'root',
    'login_password': 'hogehoge',

    'operation_name': 'テストoperation',
    'scheduled_date': '2021/10/30 20:17',
}

class ApiBuilder管理コンソールのロールメニュー紐付管理(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100000209', 'EDIT')


    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '復活',
                '項番': '2100160002',       # メニュー項目作成情報
            },
            {
                '実行処理種別': '復活',
                '項番': '2100160003',       # メニュー作成実行
            },
            {
                '実行処理種別': '復活',
                '項番': '2100020304',       # ロール名管理
            }
        ]


api_invoker = ita.ApiInvoker(ita.ApiContext())
api_invoker.invoke(params, ApiBuilder管理コンソールのロールメニュー紐付管理())
