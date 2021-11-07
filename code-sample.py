import exastro_api.ita.v1 as ita
import json
import functools

from jsonpath_ng.ext import parse
from typing import *


json_data: List[Dict[str, str]] = [
    {
        "id": "0",
        "name": "foo",
        "age": "10",
        "管理システム項番": "10"
    },
    {
        "id": "1",
        "name": "foo",
        "age": "20",
        "管理システム項番": "10"
    },
    {
        "id": "2",
        "name": "bar",
        "age": "30",
        "管理システム項番": "10"
    },
]

#jsonpath_expr = parse('$[*].?("name"="foo" & "age"="10")')
jsonpath_expr = parse('$[?(@."name"="foo" & @."age"="10")].id,name')
matches = jsonpath_expr.find(json_data)
values = [match.value for match in matches]

print(functools.reduce(lambda x, y: x + ':' +  y, values))

# 結果を表示
print( [match.value for match in matches] )


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
    'upload_file': 'upload-file.zip',
    'role_package_include_order': '1',
    'role_name': 'data_collector',
}


item_values: List[ita.ItemValue] = [
    ita.Query('2100020306', '$[?(@."Movement名"="{}")]."MovementID","Movement名"'.format(params['movement_name'])),
    ita.Join([
        ita.Query('2100020303', '$[?(@."ロールパッケージ名"="{}")]."項番","ロールパッケージ名"'.format(params['role_package_name'])),
        ita.Query('2100020304', '$[?(@."ロールパッケージ名"="{}" & @."ロール名"="{}")]."項番","ロール名"'.format(params['role_package_name'], params['role_name'])),
    ]),
]

api_context = ita.ApiContext()
for item_value in item_values:
    print('value ... ' + item_value.to_value(api_context))