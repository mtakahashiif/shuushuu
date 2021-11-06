from typing import *

json_data: List[Dict[str, str]] = [
    {
        "id": "登録",
        "実行\"処理種別": "登録",
        "管理システム項番": "10"
    },
    {
        "id": "廃止",
        "実行\"処理種別": "廃止",
        "管理システム項番": "20"
    }
]




import json
#from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

# fooリスト以下のbaz要素を検索
#jsonpath_expr = parse('$[?(@."実行\\"処理種別"="登録")]."管理システム項番"')
jsonpath_expr = parse('$[?(@."ホスト名"="target")]."管理システム項番"')
matches = jsonpath_expr.find(json_data)

# 結果を表示
print( [match.value for match in matches] )



data = r'''
{
  "status": "SUCCEED",
  "resultdata": {
    "CONTENTS": {
      "RECORD_LENGTH": 1,
      "BODY": [
        [
          "実行処理種別",
          "廃止",
          "管理システム項番",
          "HW機器種別",
          "ホスト名",
          "IPアドレス",
          "EtherWakeOnLan/MACアドレス",
          "EtherWakeOnLan/ネットワークデバイス名",
          "ログインユーザID",
          "ログインパスワード/管理",
          "ログインパスワード/ログインパスワード",
          "ssh鍵認証情報/ssh秘密鍵ファイル",
          "ssh鍵認証情報/パスフレーズ",
          "Ansible利用情報/Legacy/Role利用情報/認証方式",
          "Ansible利用情報/Legacy/Role利用情報/WinRM接続情報/ポート番号",
          "Ansible利用情報/Legacy/Role利用情報/WinRM接続情報/サーバー証明書",
          "Ansible利用情報/Pioneer利用情報/プロトコル",
          "Ansible利用情報/Pioneer利用情報/OS種別",
          "Ansible利用情報/Pioneer利用情報/LANG",
          "Ansible利用情報/接続オプション",
          "Ansible利用情報/インベントリファイル\n追加オプション",
          "Ansible利用情報/Tower利用情報/インスタンスグループ名",
          "Ansible利用情報/Tower利用情報/接続タイプ",
          "アクセス権/アクセス許可ロール",
          "備考",
          "最終更新日時",
          "更新用の最終更新日時",
          "最終更新者"
        ],
        [
          null,
          "",
          "1",
          "SV",
          "target",
          "0.0.0.0",
          null,
          null,
          "root",
          "●",
          "",
          null,
          "",
          "パスワード認証",
          null,
          null,
          "",
          "",
          "",
          null,
          null,
          "",
          "machine",
          "",
          null,
          "2021/11/02 00:25:11",
          "T_20211102002511490716",
          "システム管理者"
        ]
      ],
      "UPLOAD_FILE": {
        "1": {
          "11": "",
          "15": ""
        }
      }
    }
  }
}
'''[1:-1]


data_object = json.loads(data)

keys: List[str] = []
converted: List[Dict[str, str]] = []
for entry in data_object['resultdata']['CONTENTS']['BODY']:
    if keys:
        keys = entry
        continue

    converted_entry: Dict[str, str] = {}
    for index in range(len(keys)):
        converted_entry[keys[index]] = entry[index]

    converted.append(converted_entry)

print(converted)

jsonpath_expr = parse(r'$[?(@."ホスト名"=~"targe.")]."管理システム項番","ホスト名"')
matches = jsonpath_expr.find(converted)
print(type(matches))

# 結果を表示
print( [match.value for match in matches] )


class Builder:

    def __init__(self):
        self.entries: List[Dict[str, Any]] = []


    def build(self):
        for entry in self.entries:
            for key, value in entry.items():
                if callable(value):
                    value = value()
                
                print(key + ': ' + value)

class Join:
    def __init__(self, separator: str, callables: List[Callable[[], List[str]]]) -> None:
        self.separator: str = separator
        self.callables: List[Callable[[], List[str]]] = callables
      
    def __call__(self) -> str:
        result: str = ''

        separator: str = ''
        for callable in self.callables:
            for value in callable():
                result += separator + value
                separator = self.separator

        return result


class Query:
    def __init__(self, menu_id: str, query_string: str):
        self.menu_id: str = menu_id
        self.query_string: str = query_string

    def __call__(self) -> List[str]:
        return [ 'vvv' for i in range(int(self.menu_id)) ]


builder = Builder()

builder.entries.append({
    'id': '10',
    'value': '100'
})

builder.entries.append({
    'id': '20',
    'value': Join(':', [
        Query('1', 'xxx'),
        Query('2', 'yyy'),
        Query('2', 'zzz')
    ])
})

builder.entries.append({
    'id': '30',
    'value': '300'
})

builder.entries.append({
    'id': '20',
    'value': Join(':', [
        Query('2', 'aaa'),
        Query('1', 'bbb'),
        Query('3', 'ccc')
    ])
})


builder.build()