from .framework import *

class HardCodedColumnMetadataFinder:

    def find(self, id):
        column_names, file_upload_column_names = getattr(self, 'find_{}'.format(id))()

        return ColumnMetadata(id, column_names, file_upload_column_names)


    # 管理コンソール > メニュー管理
    def find_2100000205(self):
        column_names = [
            '実行処理種別',                     # 
            '廃止',                             # 
            'メニューID',                       # 
            'メニューグループ/ID',              # 
            'メニューグループ/名称',            # 
            'メニューグループ（ID:名称）',      # 
            'メニュー名称',                     # 
            '認証要否',                         # 
            'サービス状態',                     # 
            'メニューグループ内表示順序',       # 
            'オートフィルタチェック',           # 
            '初回フィルタ',                     # 
            'Web表示最大行数',                  # 
            'Web表示前確認行数',                # 
            'Excel出力最大行数',                # 
            'アクセス権/アクセス許可ロール',    # 
            '備考',                             # 
            '最終更新日時',                     # 
            '更新用の最終更新日時',             # 
            '最終更新者'                        # 
        ]

        return column_names, []


    # 管理コンソール > ユーザ管理
    def find_2100000208(self):
        column_names = [
            '実行処理種別',                     #  0
            '廃止',                             #  1
            'ユーザID',                         #  2
            'ログインID',                       #  3
            'ログインPW',                       #  4
            'ユーザ名',                         #  5
            'メールアドレス',                   #  6
            'パスワード無期限設定',             #  7
            '初回パスワード再設定無効',         #  8
            'PW最終更新日時',                   #  9
            '最終ログイン日時',                 # 10
            'PWカウンタ',                       # 11
            'ロック日時',                       # 12
            '認証方式',                         # 13
            '認証プロバイダー',                 # 14
            '認証プロバイダーユーザーID',       # 15
            'アクセス権/アクセス許可ロール',    # 16
            '備考',                             # 17
            '最終更新日時',                     # 18
            '更新用の最終更新日時',             # 19
            '最終更新者'                        # 20
        ]

        return column_names, []


    # 管理コンソール > ロール・メニュー紐付管理
    def find_2100000209(self):
        column_names = [
            '実行処理種別',                             #  0
            '廃止',                                     #  1
            '項番',                                     #  2
            'ロール/ID',                                #  3
            'ロール/名称',                              #  4
            'ロール（ID:名称）',                        #  5
            'メニューグループ/ID',                      #  6
            'メニューグループ/名称',                    #  7
            'メニュー/ID',                              #  8
            'メニュー/名称',                            #  9
            'メニューグループ:メニュー',                # 10
            '紐付',                                     # 11
            'アクセス権/アクセス許可ロール',            # 12
            '備考',                                     # 13
            '最終更新日時',                             # 14
            '更新用の最終更新日時',                     # 15
            '最終更新者'                                # 16
        ]

        return column_names, []


    # 基本コンソール > 機器一覧
    def find_2100000303(self):
        column_names = [
            '実行処理種別',                                                     #  0
            '廃止',                                                             #  1
            '管理システム項番',                                                 #  2
            'HW機器種別',                                                       #  3
            'ホスト名',                                                         #  4
            'IPアドレス',                                                       #  5
            'EtherWakeOnLan/MACアドレス',                                       #  6
            'EtherWakeOnLan/ネットワークデバイス名',                            #  7
            'ログインユーザID',                                                 #  8
            'ログインパスワード/管理',                                          #  9
            'ログインパスワード/ログインパスワード',                            # 10
            'ssh鍵認証情報/ssh秘密鍵ファイル',                                  # 11
            'ssh鍵認証情報/パスフレーズ',                                       # 12
            'Ansible利用情報/Legacy/Role利用情報/認証方式',                     # 13
            'Ansible利用情報/Legacy/Role利用情報/WinRM接続情報/ポート番号',     # 14
            'Ansible利用情報/Legacy/Role利用情報/WinRM接続情報/サーバー証明書', # 15
            'Ansible利用情報/Pioneer利用情報/プロトコル',                       # 16
            'Ansible利用情報/Pioneer利用情報/OS種別',                           # 17
            'Ansible利用情報/Pioneer利用情報/LANG',                             # 18
            'Ansible利用情報/接続オプション',                                   # 19
            'Ansible利用情報/インベントリファイル\n追加オプション',             # 20
            'Ansible利用情報/Tower利用情報/インスタンスグループ名',             # 21
            'Ansible利用情報/Tower利用情報/接続タイプ',                         # 22
            'アクセス権/アクセス許可ロール',                                    # 23
            '備考',                                                             # 24
            '最終更新日時',                                                     # 25
            '更新用の最終更新日時',                                             # 26
            '最終更新者'                                                        # 27
        ]

        file_upload_column_names = [
            'ssh鍵認証情報/ssh秘密鍵ファイル'
        ]

        return column_names, file_upload_column_names


    # 基本コンソール > オペレーション一覧
    def find_2100000304(self):
        column_names = [
            '実行処理種別',                     #  0
            '廃止',                             #  1
            'No.',                              #  2
            'オペレーションID',                 #  3
            'オペレーション名',                 #  4
            '実施予定日時',                     #  5
            '最終実行日時',                     #  6
            'アクセス権/アクセス許可ロール',    #  7
            '備考',                             #  8
            '最終更新日時',                     #  9
            '更新用の最終更新日時',             # 10
            '最終更新者'                        # 11
        ]

        return column_names, []


    # メニュー作成 > メニュー項目作成情報
    def find_2100160002(self):
        column_names = [
            '実行処理種別',                                     #  0
            '廃止',                                             #  1
            '項番',                                             #  2
            'メニュー名',                                       #  3
            '項目名',                                           #  4
            '表示順序',                                         #  5
            '必須',                                             #  6
            '一意制約',                                         #  7
            'カラムグループ',                                   #  8
            '入力方式',                                         #  9
            '文字列(単一行)/最大バイト数',                      # 10
            '文字列(単一行)/正規表現',                          # 11
            '文字列(複数行)/最大バイト数',                      # 12
            '文字列(複数行)/正規表現',                          # 13
            '整数/最小値',                                      # 14
            '整数/最大値',                                      # 15
            '小数/最小値',                                      # 16
            '小数/最大値',                                      # 17
            '小数/桁数',                                        # 18
            'プルダウン選択/メニューグループ：メニュー：項目',  # 19
            'プルダウン選択/参照項目',                          # 20
            'パスワード/最大バイト数',                          # 21
            'ファイルアップロード/ファイル最大バイト数',        # 22
            'リンク/最大バイト数',                              # 23
            '説明',                                             # 24
            'アクセス権/アクセス許可ロール',                    # 25
            '備考',                                             # 26
            '最終更新日時',                                     # 27
            '更新用の最終更新日時',                             # 28
            '最終更新者'                                        # 29
        ]

        return column_names, []


    # Ansible共通 > 収集インターフェース情報
    def find_2100040709(self):
        column_names = [
            '実行処理種別',                     #  0
            'ID',                               #  1
            'ホスト名',                         #  2
            'IP',                               #  3
            'RESTユーザー',                     #  4
            'RESTパスワード',                   #  5
            'REST方式',                         #  6
            'プロトコル',                       #  7
            'ポート',                           #  8
            'アクセス権/アクセス許可ロール',    #  9
            '備考',                             # 10
            '最終更新日時',                     # 11
            '更新用の最終更新日時',             # 12
            '最終更新者'                        # 13
        ]

        return column_names, []


    # Ansible共通 > 収集項目値管理
    def find_2100040710(self):
        column_names = [
            '実行処理種別',                                         #  0
            '廃止',                                                 #  1
            'ID',                                                   #  2
            '収集項目(FROM)/パース形式',                            #  3
            '収集項目(FROM)/PREFIX(ファイル名)',                    #  4
            '収集項目(FROM)/変数名',                                #  5
            '収集項目(FROM)/メンバ変数',                            #  6
            'パラメータシート(TO)/メニューグループ:メニュー:項目',  #  7
            'アクセス権/アクセス許可ロール',                        #  8
            '備考',                                                 #  9
            '最終更新日時',                                         # 10
            '更新用の最終更新日時',                                 # 11
            '最終更新者'                                            # 12
        ]

        return column_names, []


    # Ansible-Legacy > Movement一覧
    def find_2100020103(self):
        column_names = [
            '実行処理種別',                             #  0
            '廃止',                                     #  1
            'MovementID',                               #  2
            'Movement名',                               #  3
            'オーケストレータ',                         #  4
            '遅延タイマー',                             #  5
            'Ansible利用情報/ホスト指定形式',           #  6
            'Ansible利用情報/WinRM接続',                #  7
            'Ansible利用情報/virtualenv',               #  8
            'Ansible利用情報/ヘッダーセクション',       #  9
            'Ansible利用情報/オプションパラメータ',     # 10
            'アクセス権/アクセス許可ロール',            # 11
            '備考',                                     # 12
            '最終更新日時',                             # 13
            '更新用の最終更新日時',                     # 14
            '最終更新者'                                # 15
        ]

        return column_names, []


    # Ansible-Legacy > Playbook素材集
    def find_2100020104(self):
        column_names = [
            '実行処理種別',                     # 0
            '廃止',                             # 1
            '素材ID',                           # 2
            'Playbook素材名',                   # 3
            'Playbook素材',                     # 4
            'アクセス権/アクセス許可ロール',    # 5
            '備考',                             # 6
            '最終更新日時',                     # 7
            '更新用の最終更新日時',             # 8
            '最終更新者'                        # 9
        ]

        file_upload_column_names = [
            'Playbook素材'
        ]

        return column_names, file_upload_column_names


    # Ansible-Legacy > Movement-Playbook紐付
    def find_2100020105(self):
        column_names = [
            '実行処理種別',                     #  0
            '廃止',                             #  1
            '紐付項番',                         #  2
            'Movement',                         #  3
            'Playbook素材',                     #  4
            'インクルード順序',                 #  5
            'アクセス権/アクセス許可ロール',    #  6
            '備考',                             #  7
            '最終更新日時',                     #  8
            '更新用の最終更新日時',             #  9
            '最終更新者'                        # 10
        ]

        return column_names, []


    # Ansible-Legacy > Movement-Playbook紐付
    def find_2100020108(self):
        column_names = [
            '実行処理種別',                     #  0
            '廃止',                             #  1
            '項番',                             #  2
            'オペレーション',                   #  3
            'Movement',                         #  4
            'ホスト',                           #  5
            'アクセス権/アクセス許可ロール',    #  6
            '備考',                             #  7
            '最終更新日時',                     #  8
            '更新用の最終更新日時',             #  9
            '最終更新者'                        # 10
        ]

        return column_names, []


    # Ansible-LegacyRole > Movement一覧
    def find_2100020306(self):
        column_names = [
            '実行処理種別',                             #  0
            '廃止',                                     #  1
            'MovementID',                               #  2
            'Movement名',                               #  3
            'オーケストレータ',                         #  4
            '遅延タイマー',                             #  5
            'Ansible利用情報/ホスト指定形式',           #  6
            'Ansible利用情報/WinRM接続',                #  7
            'Ansible利用情報/ヘッダーセクション',       #  8
            'Ansible利用情報/オプションパラメータ',     #  9
            'アクセス権/アクセス許可ロール',            # 10
            '備考',                                     # 11
            '最終更新日時',                             # 12
            '更新用の最終更新日時',                     # 13
            '最終更新者'                                # 14
        ]

        return column_names, []


    # Ansible-LegacyRole > ロールパッケージ管理
    def find_2100020303(self):
        column_names = [
            '実行処理種別',                         #  0
            '廃止',                                 #  1
            '項番',                                 #  2
            'ロールパッケージ名',                   #  3
            'ロールパッケージファイル(ZIP形式)',    #  4
            'アクセス権/アクセス許可ロール',        #  5
            '備考',                                 #  6
            '最終更新日時',                         #  7
            '更新用の最終更新日時',                 #  8
            '最終更新者'                            #  9
        ]

        file_upload_column_names = [
            'ロールパッケージファイル(ZIP形式)'
        ]

        return column_names, file_upload_column_names


    # Ansible-LegacyRole > ロール名管理
    def find_2100020304(self):
        column_names = [
            '実行処理種別',                     # 0
            '廃止',                             # 1
            '項番',                             # 2
            'ロールパッケージ名',               # 3
            'ロール名',                         # 4
            'アクセス権/アクセス許可ロール',    # 5
            '備考',                             # 6
            '最終更新日時',                     # 7
            '更新用の最終更新日時',             # 8
            '最終更新者'                        # 9
        ]

        return column_names, []


    # Ansible-LegacyRole > Movement-ロール紐付
    def find_2100020307(self):
        column_names = [
            '実行処理種別',                     #  0
            '廃止',                             #  1
            '紐付項番',                         #  2
            'Movement',                         #  3
            'ロールパッケージ名：ロール名',     #  4
            'インクルード順序',                 #  5
            'アクセス権/アクセス許可ロール',    #  6
            '備考',                             #  7
            '最終更新日時',                     #  8
            '更新用の最終更新日時',             #  9
            '最終更新者'                        # 10
        ]

        return column_names, []


    # Ansible-LegacyRole > 作業対象ホスト
    def find_2100020310(self):
        column_names = [
            '実行処理種別',                     #  0
            '廃止',                             #  1
            '項番',                             #  2
            'オペレーション',                   #  3
            'Movement',                         #  4
            'ホスト',                           #  5
            'アクセス権/アクセス許可ロール',    #  6
            '備考',                             #  7
            '最終更新日時',                     #  8
            '更新用の最終更新日時',             #  9
            '最終更新者'                        # 10
        ]

        return column_names, []


    # CI/CD for IaC > リモートリポジトリ
    def find_2100120001(self):
        column_names = [
            '実行処理種別',                             #  0
            '廃止',                                     #  1
            '項番',                                     #  2
            'リモートリポジトリ名',                     #  3
            'リモートリポジトリ(URL)',                  #  4
            'ブランチ',                                 #  5
            'プロトコル',                               #  6
            'Visibilityタイプ',                         #  7
            'Git アカウント情報/ユーザ',                #  8
            'Git アカウント情報/パスワード',            #  9
            'ssh接続情報/パスワード',                   # 10
            'ssh接続情報/パスフレーズ',                 # 11
            'ssh接続情報/接続パラメータ',               # 12
            'Proxy/Address',                            # 13
            'Proxy/Port',                               # 14
            'リモートリポジトリ同期情報/自動同期',      # 15
            'リモートリポジトリ同期情報/周期(秒)',      # 16
            'リモートリポジトリ同期状態/状態',          # 17
            'リモートリポジトリ同期状態/詳細情報',      # 18
            '通信リトライ情報/回数',                    # 19
            '通信リトライ情報/周期(ms)',                # 20
            'アクセス権/アクセス許可ロール',            # 21
            '備考',                                     # 22
            '最終更新日時',                             # 23
            '更新用の最終更新日時',                     # 24
            '最終更新者'                                # 25
        ]

        return column_names, []


    # CI/CD for IaC > 登録アカウント
    def find_2100120005(self):
        column_names = [
            '実行処理種別',                                 # 0
            '廃止',                                         # 1
            '項番',                                         # 2
            'Exastro IT Automationアカウント/ログインID',   # 3
            'Exastro IT Automationアカウント/ログインPW',   # 4
            'アクセス権/アクセス許可ロール',                # 5
            '備考',                                         # 6
            '最終更新日時',                                 # 7
            '更新用の最終更新日時',                         # 8
            '最終更新者'                                    # 9
        ]

        return column_names, []


    # CI/CD for IaC > 資材紐付
    def find_2100120003(self):
        column_names = [
            '実行処理種別',                                         #  0
            '廃止',                                                 #  1
            '項番',                                                 #  2
            '紐付先資材名',                                         #  3
            'Git リポジトリ(From)/資材パス',                        #  4
            'Exastro IT automation(To)/紐付先資材タイプ',           #  5
            'Exastro IT automation(To)/テンプレート管理/変数定義',  #  6
            'Exastro IT automation(To)/Ansible-Pioneer/対話種別',   #  7
            'Exastro IT automation(To)/Ansible-Pioneer/OS種別',     #  8
            'Exastro IT automation(To)/実行ログインID',             #  9
            'Exastro IT automation(To)/アクセス許可ロール付与',     # 10
            '素材同期情報/自動同期',                                # 11
            '素材同期情報/状態',                                    # 12
            '素材同期情報/詳細情報',                                # 13
            '素材同期情報/最終日時',                                # 14
            '素材同期情報/最終実行ログインID',                      # 15
            'デリバリ情報/オペレーション',                          # 16
            'デリバリ情報/Movement',                                # 17
            'デリバリ情報/ドライラン',                              # 18
            'デリバリ情報/詳細情報',                                # 19
            'デリバリ情報/作業インスタンスNo',                      # 20
            'アクセス権/アクセス許可ロール',                        # 21
            '備考',                                                 # 22
            '最終更新日時',                                         # 23
            '更新用の最終更新日時',                                 # 24
            '最終更新者'                                            # 25
        ]

        return column_names, []
