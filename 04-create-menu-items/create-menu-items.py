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


class ApiBuilderメニュー作成のメニュー項目作成情報(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100160002', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        entries = []

        index_counter = ita.SimpleIndexCounter()
        for yaml_type in ['文字列', '整数', '浮動小数点', 'ブーリアン', 'ヌル']:
            entries += [
                {
                    '実行処理種別': '登録',
                    'メニュー名': params['menu_name'],
                    '項目名': '{}_to_文字列(単一行)'.format(yaml_type),
                    '表示順序': index_counter(),
                    '入力方式': '文字列(単一行)',
                    '文字列(単一行)/最大バイト数': 64
                },
                {
                    '実行処理種別': '登録',
                    'メニュー名': params['menu_name'],
                    '項目名': '{}_to_文字列(複数行)'.format(yaml_type),
                    '表示順序': index_counter(),
                    '入力方式': '文字列(複数行)',
                    '文字列(複数行)/最大バイト数': 64
                },
                {
                    '実行処理種別': '登録',
                    'メニュー名': params['menu_name'],
                    '項目名': '{}_to_整数'.format(yaml_type),
                    '表示順序': index_counter(),
                    '入力方式': '整数',
                },
                {
                    '実行処理種別': '登録',
                    'メニュー名': params['menu_name'],
                    '項目名': '{}_to_小数'.format(yaml_type),
                    '表示順序': index_counter(),
                    '入力方式': '小数',
                },
                {
                    '実行処理種別': '登録',
                    'メニュー名': params['menu_name'],
                    '項目名': '{}_to_日時'.format(yaml_type),
                    '表示順序': index_counter(),
                    '入力方式': '日時',
                },
                {
                    '実行処理種別': '登録',
                    'メニュー名': params['menu_name'],
                    '項目名': '{}_to_日付'.format(yaml_type),
                    '表示順序': index_counter(),
                    '入力方式': '日付',
                },
                {
                    '実行処理種別': '登録',
                    'メニュー名': params['menu_name'],
                    '項目名': '{}_to_パスワード'.format(yaml_type),
                    '表示順序': index_counter(),
                    '入力方式': 'パスワード',
                    'パスワード/最大バイト数': 64
                },
                {
                    '実行処理種別': '登録',
                    'メニュー名': params['menu_name'],
                    '項目名': '{}_to_リンク'.format(yaml_type),
                    '表示順序': index_counter(),
                    '入力方式': 'リンク',
                    'リンク/最大バイト数': 64
                }
            ]
            
        return entries


api_invoker = ita.ApiInvoker(ita.ApiContext())
api_invoker.invoke(params, ApiBuilderメニュー作成のメニュー項目作成情報())
