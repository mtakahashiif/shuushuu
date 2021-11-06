import exastro_api.ita.v1 as ita


class Params:
    def __init__(self):
        self.hostname = 'target'
        self.ip_address = '0.0.0.0'     # dummy
        self.login_username = 'root'
        self.login_password = 'hogehoge'

        self.operation_name = 'テストoperation'
        self.scheduled_date = '2021/10/30 20:17'
        
        self.menu_name = 'テスト用メニュー'


class ApiBuilder管理コンソールのロールメニュー紐付管理(ita.ApiBuilder):
    def __init__(self):
        super().__init__('2100000209', 'EDIT')

    def build(self, params):
        self.add_entry({
            '実行処理種別': '復活',
            '項番': '2100160002',       # メニュー項目作成情報
        })

        self.add_entry({
            '実行処理種別': '復活',
            '項番': '2100160003',       # メニュー作成実行
        })


api_invoker = ita.ApiInvoker(ita.ApiContext())
api_invoker.add_builder(ApiBuilder管理コンソールのロールメニュー紐付管理())
api_invoker.invoke(Params())
