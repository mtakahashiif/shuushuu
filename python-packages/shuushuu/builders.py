import exastro_api.ita.v1 as ita

from typing import *


def column_name_matrix() -> Iterator[Tuple[str, str, str]]:
    for yaml_type in ['文字列', '整数', '浮動小数点', 'ブーリアン', 'ヌル']:
#        for column_type in ['文字列(単一行)', '文字列(複数行)', '整数', '小数', '日時', '日付', 'パスワード', 'リンク']:
        for column_type in ['文字列(単一行)', '文字列(複数行)', '整数', '小数']:
            yield '{}_to_{}'.format(yaml_type, column_type.translate(str.maketrans('(', '_', ')'))), yaml_type, column_type


class ApiBuilder管理コンソールのロールメニュー紐付管理(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100000209', 'EDIT')


    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '復活',
                '項番': '2100160002',                               # メニュー項目作成情報
                '更新用の最終更新日時': 'T_20150401100000000000'    # WORKAROUND 現時点ではハードコード
            },
            {
                '実行処理種別': '復活',
                '項番': '2100160003',                               # メニュー作成実行
                '更新用の最終更新日時': 'T_20150401100000000000'    # WORKAROUND 現時点ではハードコード
            },
            {
                '実行処理種別': '復活',
                '項番': '2100020304',                               # ロール名管理
                '更新用の最終更新日時': 'T_20150401100000000000'    # WORKAROUND 現時点ではハードコード
            }
        ]


class ApiBuilderメニュー作成のメニュー項目作成情報(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100160002', 'EDIT')


    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        entries = []

        extras: Dict[str, Dict[str, str]] = {
            '文字列(単一行)': { '文字列(単一行)/最大バイト数': '64' }, 
            '文字列(複数行)': { '文字列(複数行)/最大バイト数': '64' },
            '整数': {},
            '小数': {},
            '日時': {},
            '日付': {},
            'パスワード': { 'パスワード/最大バイト数': '64' },
            'リンク': { 'リンク/最大バイト数': '64' }
        }

        index_counter = ita.SimpleIndexCounter()
        for column_name, _, column_type in column_name_matrix():
            entries.append({
                '実行処理種別': '登録',
                'メニュー名': params['メニュー名'],
                '項目名': column_name,
                '表示順序': index_counter(),
                '入力方式': column_type,
                **extras[column_type]
            })
            
        return entries


class ApiBuilder基本コンソールの機器一覧(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100000303', 'EDIT')


    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'HW機器種別': 'SV',
                'ホスト名': params['対象ホストのホスト名'],
                'IPアドレス': params['対象ホストのIPアドレス'],
                'ログインユーザID': params['対象ホストのログインユーザID'],
                'ログインパスワード/管理': '●',
                'ログインパスワード/ログインパスワード': params['対象ホストのログインパスワード'],
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
                'オペレーション名': params['オペレーション名'],
                '実施予定日時': params['オペレーションの実施予定日時'],
            }
        ]


class ApiBuilderAnsibleLegacyRoleのMovement一覧(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020306', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'Movement名': params['Movement名'],
                'Ansible利用情報/ホスト指定形式': 'ホスト名',
                'Ansible利用情報/ヘッダーセクション': params['Movementのヘッダセクション']
            }
        ]


class ApiBuilderAnsibleLegacyRoleのロールパッケージ管理(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020303', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'ロールパッケージ名': params['データ収集ロールのパッケージ名'],
                'ロールパッケージファイル(ZIP形式)': ita.UploadFile(params['データ収集ロールのzipファイルパス'])
            }
        ]


class ApiBuilderAnsibleLegacyRoleのMovementロール紐付(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020307', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                "Movement": ita.Query('2100020306', '$[?(@."Movement名"="{}" & @."廃止"!="廃止")]."MovementID","Movement名"'.format(params['Movement名'])),
                "ロールパッケージ名：ロール名": ita.Join([
                    ita.Query('2100020303', '$[?(@."ロールパッケージ名"="{}" & @."廃止"!="廃止")]."項番","ロールパッケージ名"'.format(params['データ収集ロールのパッケージ名'])),
                    ita.Query('2100020304', '$[?(@."ロールパッケージ名"="{}" & @."ロール名"="{}" & @."廃止"!="廃止")]."項番","ロール名"'.format(params['データ収集ロールのパッケージ名'], params['データ収集ロールのロール名']))
                ]),
                "インクルード順序": params['データ収集ロールのインクルード順序']
            }
        ]


class ApiBuilderAnsibleLegacyRoleの作業対象ホスト(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020310', 'EDIT')


    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                "オペレーション": ita.Query('2100000304', '$[?(@."オペレーション名"="{}" & @."廃止"!="廃止")]."オペレーションID","オペレーション名"'.format(params['オペレーション名'])),
                "Movement": ita.Query('2100020306', '$[?(@."Movement名"="{}" & @."廃止"!="廃止")]."MovementID","Movement名"'.format(params['Movement名'])),
                "ホスト": ita.Query('2100000303', '$[?(@."ホスト名"="{}" & @."廃止"!="廃止")]."管理システム項番","ホスト名"'.format(params['対象ホストのホスト名'])),
            }
        ]


class ApiBuilderAnsible共通の収集項目値管理(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100040710', 'EDIT')


    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        excluded_column_names = [
            '文字列_to_整数',
            '文字列_to_小数',
            '浮動小数点_to_整数'
        ]

        entries = []
        for column_name, _, _ in column_name_matrix():
            if column_name in excluded_column_names:
                continue

            # 項目"パラメータシート(TO)/メニューグループ:メニュー:項目"の具体例は以下。
            #   "2100011611:代入値自動登録用:2:データ収集メニュー:2:パラメータ/文字列_to_文字列(単一行)"
            #
            # WORKAROUND
            # カラムグループを考慮したメニューの項目名、例えば"パラメータ/接続情報/ユーザ名"の
            # ような項目名を項目名のIDと紐づけて取得することは、REST APIでは困難なので、項目名の
            # 先頭に固定的に"パラメータ/"を付与することで回避する。この方法では独自のカラムグループに
            # 含まれる項目名は指定できないという制限がある。
            entries.append({
                '実行処理種別': '登録',
                '収集項目(FROM)/パース形式': 'YAML',
                '収集項目(FROM)/PREFIX(ファイル名)': 'collected-data',
                '収集項目(FROM)/変数名': column_name,
                'パラメータシート(TO)/メニューグループ:メニュー:項目': ita.Join([
                    ita.Query('2100000205', '$[?(@."メニューグループ/名称"="代入値自動登録用" & @."メニュー名称"="{}" & @."廃止"!="廃止")]."メニューグループ/ID","メニューグループ/名称","メニューID","メニュー名称"'.format(params['メニュー名'])),
                    ita.Query('2100160002', '$[?(@."メニュー名"="{}" & @."項目名"="{}" & @."廃止"!="廃止")]."項番","項目名"'.format(params['メニュー名'], column_name), ":パラメータ/")
                ])
            })

        return entries


class ApiBuilderAnsible共通の収集インターフェース情報(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100040709', 'EDIT')


    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '更新',
                'ID': '1',
                'RESTユーザー': params['REST_APIユーザ名'],
                'RESTパスワード': params['REST_APIパスワード'],
                '更新用の最終更新日時': 'T_20150401100000000000'
            }
        ]
