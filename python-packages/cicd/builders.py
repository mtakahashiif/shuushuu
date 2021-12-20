import exastro_api.ita.v1 as ita

from typing import *

from exastro_api.ita.v1.framework import StrText


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


class ApiBuilderAnsibleLegacyのMovement一覧(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020103', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'Movement名': params['Movement名'],
                'Ansible利用情報/ホスト指定形式': 'ホスト名',
            }
        ]


class ApiBuilderAnsibleLegacyのPlaybook素材集(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020104', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'Playbook素材名': params['Playbook素材名'],
                'Playbook素材': ita.UploadFile(params['Playbook素材のファイルパス'])
            }
        ]


class ApiBuilderAnsibleLegacyのMovementPlaybook紐付(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020105', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'Movement': ita.Query('2100020103', '$[?(@."Movement名"="{}" & @."廃止"!="廃止")]."MovementID","Movement名"'.format(params['Movement名'])),
                'Playbook素材': params['Playbook素材名'],
                'インクルード順序': params['Playbookのインクルード順序']
            }
        ]


class ApiBuilderAnsibleLegacyの作業対象ホスト(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020108', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'オペレーション': ita.Query('2100000304', '$[?(@."オペレーション名"="{}" & @."廃止"!="廃止")]."オペレーションID","オペレーション名"'.format(params['オペレーション名'])),
                'Movement': ita.Query('2100020103', '$[?(@."Movement名"="{}" & @."廃止"!="廃止")]."MovementID","Movement名"'.format(params['Movement名'])),
                'ホスト': ita.Query('2100000303', '$[?(@."ホスト名"="{}" & @."廃止"!="廃止")]."管理システム項番","ホスト名"'.format(params['対象ホストのホスト名'])),
            }
        ]


class ApiBuilderCICDforIaCのリモートリポジトリ(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100120001', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'リモートリポジトリ名': params['Gitリポジトリの名前'],
                'リモートリポジトリ(URL)': params['GitリポジトリのURL'],
                'プロトコル': params['Gitリポジトリのプロトコル'],
                'Visibilityタイプ': params['Gitリポジトリの可視性'],
                'リモートリポジトリ同期情報/自動同期': params['Gitリポジトリの同期'],
                'リモートリポジトリ同期情報/周期(秒)': params['Gitリポジトリの同期の周期']
            }
        ]


class ApiBuilderCICDforIaCの登録アカウント(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100120005', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'Exastro IT Automationアカウント/ログインID': ita.Query('2100000208', '$[?(@."ログインID"="{}" & @."廃止"!="廃止")]."ユーザID","ログインID"'.format(params['REST_APIユーザ名'])),
                'Exastro IT Automationアカウント/ログインPW': params['REST_APIパスワード'],
            }
        ]


class ApiBuilderCICDforIaCの資材紐付(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100120003', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                '紐付先資材名': params['httpdのGit紐付けの名前'],
                'Git リポジトリ(From)/資材パス': '{}:{}'.format(params['Gitリポジトリの名前'], params['httpdのGit紐付けの資材パス']),
                'Exastro IT automation(To)/紐付先資材タイプ': params['httpdのGit紐付けの資材タイプ'],
                'Exastro IT automation(To)/実行ログインID': params['httpdのGit紐付けの実行ログインID'],
#                'Exastro IT automation(To)/実行ログインID': ita.Join([
#                    ita.Query(
#                        '2100120005',
#                        '$[?(@."Exastro IT Automationアカウント/ログインID"="{}" & @."廃止"!="廃止")]."項番"'.format(
#                            ita.Query('2100000208', '$[?(@."ログインID"="{}" & @."廃止"!="廃止")]."ユーザID","ログインID"'.format(params['REST_APIユーザ名'])),
#                        )
#                    ),
#                    ita.StrText(params['REST_APIユーザ名'])
#                ]),
                '素材同期情報/自動同期': params['httpdのGit紐付けの同期'],
#                'デリバリ情報/オペレーション': params['オペレーション名'],
#                'デリバリ情報/Movement': '{}:{}'.format(params['Movementのオーケストレータ'], params['Movement名']),
#                'デリバリ情報/ドライラン': params['httpdのGit紐付けのドライランフラグ'],
            }
        ]


class ApiBuilderAnsibleLegacyのMovementPlaybook紐付2(ita.ApiBuilder):
    def __init__(self) -> None:
        super().__init__('2100020105', 'EDIT')

    def create_entries(self, params: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        return [
            {
                '実行処理種別': '登録',
                'Movement': ita.Query('2100020103', '$[?(@."Movement名"="{}" & @."廃止"!="廃止")]."MovementID","Movement名"'.format(params['Movement名'])),
                'Playbook素材': params['httpdのGit紐付けの名前'],
                'インクルード順序': params['Playbookのインクルード順序']
            }
        ]
