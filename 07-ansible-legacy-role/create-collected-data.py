import sys
import yaml

values = {
    '文字列': 'hello',
    '整数': 10,
    '浮動小数点': 55.55,
    'ブーリアン': True,
    'ヌル': None
}

yaml_object = {}

for key, value in values.items():
    yaml_object['{}_to_文字列(単一行)'.format(key)] = value
    yaml_object['{}_to_文字列(複数行)'.format(key)] = value
    yaml_object['{}_to_整数'.format(key)] = value
    yaml_object['{}_to_小数'.format(key)] = value
    yaml_object['{}_to_日時'.format(key)] = value
    yaml_object['{}_to_日付'.format(key)] = value
    yaml_object['{}_to_パスワード'.format(key)] = value
    yaml_object['{}_to_リンク'.format(key)] = value

yaml.dump(yaml_object, sys.stdout, allow_unicode=True, default_flow_style=False, sort_keys=False)
