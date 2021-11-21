import os
import os.path
import shutil
import sys
import time
import yaml
from typing import *

import shuushuu
import exastro_api.ita.v1 as ita


class SubCommand:
    def __init__(self) -> None:
        self.api_context = ita.ApiContext()


    def invoke(self, name: str, params: Dict[str, str]) -> None:
        getattr(self, name)(params)


    def enable_menu(self, params: Dict[str, str]) -> None:
        api_invoker = ita.ApiInvoker(ita.ApiContext())
        api_invoker.invoke(params, shuushuu.ApiBuilder管理コンソールのロールメニュー紐付管理())


    def create_menu_items(self, params: Dict[str, str]) -> None:
        api_invoker = ita.ApiInvoker(self.api_context)
        api_invoker.invoke(params, shuushuu.ApiBuilderメニュー作成のメニュー項目作成情報())


    def create_movement(self, params: Dict[str, str]) -> None:
        # copy roles directory to workspace
        zip_contents_dir = self.api_context.create_temporary_dir('zip-contents')
        roles_path_under_current_dir = self.api_context.get_path_under_current_dir(params['データ収集ロールのパス'])
        roles_path_under_workspace = os.path.join(zip_contents_dir, params['データ収集ロールのパス'])
        shutil.copytree(roles_path_under_current_dir, roles_path_under_workspace)

        # create "roles/data_collector/files/collected-data.yml"
        collected_data_file_path = os.path.join(zip_contents_dir, 'roles/data_collector/files/collected-data.yml')
        shuushuu.create_collected_data(collected_data_file_path)

        # create roles zip file
        zip_file_path_basename = os.path.splitext(self.api_context.get_path_under_workspace(params['データ収集ロールのzipファイル名']))[0]
        zip_file_path = shutil.make_archive(zip_file_path_basename, 'zip', root_dir=zip_contents_dir)

        # set zip file path to params
        params['データ収集ロールのzipファイルパス'] = zip_file_path
        
        api_invoker = ita.ApiInvoker(self.api_context)
        api_invoker.invoke(params, shuushuu.ApiBuilder基本コンソールの機器一覧())
        time.sleep(1)
        api_invoker.invoke(params, shuushuu.ApiBuilder基本コンソールのオペレーション一覧())
        time.sleep(1)
        api_invoker.invoke(params, shuushuu.ApiBuilderAnsibleLegacyRoleのMovement一覧())
        time.sleep(1)
        api_invoker.invoke(params, shuushuu.ApiBuilderAnsibleLegacyRoleのロールパッケージ管理())
        time.sleep(10)
        api_invoker.invoke(params, shuushuu.ApiBuilderAnsibleLegacyRoleのMovementロール紐付())
        time.sleep(1)
        api_invoker.invoke(params, shuushuu.ApiBuilderAnsibleLegacyRoleの作業対象ホスト())
        time.sleep(1)
        api_invoker.invoke(params, shuushuu.ApiBuilderAnsible共通の収集項目値管理())


subcommand_name = sys.argv[1]
parameter_file = sys.argv[2]

with open(parameter_file) as file:
    params = yaml.load(file, Loader=yaml.CLoader)

subcommand = SubCommand()
subcommand.invoke(subcommand_name, params)