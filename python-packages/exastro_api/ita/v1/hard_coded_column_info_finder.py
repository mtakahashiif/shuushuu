from .framework import *

class HardCodedColumnMetadataFinder:

    def find(self, id):
        column_names, file_upload_column_names = getattr(self, 'find_{}'.format(id))()

        return ColumnMetadata(id, column_names, file_upload_column_names)


    # 管理コンソール > ロール・メニュー紐付管理
    def find_2100000209(self):
        column_names = [
            "実行処理種別",                             #  0
            "廃止",                                     #  1
            "項番",                                     #  2
            "ロール/ID",                                #  3
            "ロール/名称",                              #  4
            "ロール（ID:名称）",                        #  5
            "メニューグループ/ID",                      #  6
            "メニューグループ/名称",                    #  7
            "メニュー/ID",                              #  8
            "メニュー/名称",                            #  9
            "メニューグループ:メニュー",                # 10
            "紐付",                                     # 11
            "アクセス権/アクセス許可ロール",            # 12
            "備考",                                     # 13
            "最終更新日時",                             # 14
            "更新用の最終更新日時",                     # 15
            "最終更新者"                                # 16
        ]

        return column_names, []


    # 基本コンソール > 機器一覧
    def find_2100000303(self):
        column_names = [
            "実行処理種別",                                                     #  0
            "廃止",                                                             #  1
            "管理システム項番",                                                 #  2
            "HW機器種別",                                                       #  3
            "ホスト名",                                                         #  4
            "IPアドレス",                                                       #  5
            "EtherWakeOnLan/MACアドレス",                                       #  6
            "EtherWakeOnLan/ネットワークデバイス名",                            #  7
            "ログインユーザID",                                                 #  8
            "ログインパスワード/管理",                                          #  9
            "ログインパスワード/ログインパスワード",                            # 10
            "ssh鍵認証情報/ssh秘密鍵ファイル",                                  # 11
            "ssh鍵認証情報/パスフレーズ",                                       # 12
            "Ansible利用情報/Legacy/Role利用情報/認証方式",                     # 13
            "Ansible利用情報/Legacy/Role利用情報/WinRM接続情報/ポート番号",     # 14
            "Ansible利用情報/Legacy/Role利用情報/WinRM接続情報/サーバー証明書", # 15
            "Ansible利用情報/Pioneer利用情報/プロトコル",                       # 16
            "Ansible利用情報/Pioneer利用情報/OS種別",                           # 17
            "Ansible利用情報/Pioneer利用情報/LANG",                             # 18
            "Ansible利用情報/接続オプション",                                   # 19
            "Ansible利用情報/インベントリファイル\n追加オプション",             # 20
            "Ansible利用情報/Tower利用情報/インスタンスグループ名",             # 21
            "Ansible利用情報/Tower利用情報/接続タイプ",                         # 22
            "アクセス権/アクセス許可ロール",                                    # 23
            "備考",                                                             # 24
            "最終更新日時",                                                     # 25
            "更新用の最終更新日時",                                             # 26
            "最終更新者"                                                        # 27
        ]

        file_upload_column_names = [
            'ssh鍵認証情報/ssh秘密鍵ファイル'
        ]

        return column_names, file_upload_column_names


    # 基本コンソール > オペレーション一覧
    def find_2100000304(self):
        column_names = [
            "実行処理種別",                     #  0
            "廃止",                             #  1
            "No.",                              #  2
            "オペレーションID",                 #  3
            "オペレーション名",                 #  4
            "実施予定日時",                     #  5
            "最終実行日時",                     #  6
            "アクセス権/アクセス許可ロール",    #  7
            "備考",                             #  8
            "最終更新日時",                     #  9
            "更新用の最終更新日時",             # 10
            "最終更新者"                        # 11
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


    # Ansible-LegacyRole > Movement-ロール紐付
    def find_2100020307(self):
        column_names = [
            "実行処理種別",                     #  0
            "廃止",                             #  1
            "紐付項番",                         #  2
            "Movement",                         #  3
            "ロールパッケージ名：ロール名",     #  4
            "インクルード順序",                 #  5
            "アクセス権/アクセス許可ロール",    #  6
            "備考",                             #  7
            "最終更新日時",                     #  8
            "更新用の最終更新日時",             #  9
            "最終更新者"                        # 10
        ]

        file_upload_column_names = [
        ]

        return column_names, file_upload_column_names
