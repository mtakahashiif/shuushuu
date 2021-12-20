import os
import os.path
import shutil
import sys
import time
import yaml
from typing import *

import cicd
import exastro_api.ita.v1 as ita


class SubCommand:
    def __init__(self) -> None:
        self.api_context = ita.ApiContext()


    def invoke(self, name: str, params: Dict[str, str]) -> None:
        getattr(self, name)(params)


    def create_movement(self, params: Dict[str, str]) -> None:
        api_invoker = ita.ApiInvoker(self.api_context)
        api_invoker.invoke(params, cicd.ApiBuilder基本コンソールの機器一覧())
        api_invoker.invoke(params, cicd.ApiBuilder基本コンソールのオペレーション一覧())
        api_invoker.invoke(params, cicd.ApiBuilderAnsibleLegacyのMovement一覧())

#        api_invoker.invoke(params, cicd.ApiBuilderAnsibleLegacyのPlaybook素材集())
#        api_invoker.invoke(params, cicd.ApiBuilderAnsibleLegacyのMovementPlaybook紐付())

        api_invoker.invoke(params, cicd.ApiBuilderAnsibleLegacyの作業対象ホスト())

        api_invoker.invoke(params, cicd.ApiBuilderCICDforIaCのリモートリポジトリ())
        api_invoker.invoke(params, cicd.ApiBuilderCICDforIaCの登録アカウント())
        api_invoker.invoke(params, cicd.ApiBuilderCICDforIaCの資材紐付())

        api_invoker.invoke(params, cicd.ApiBuilderAnsibleLegacyのMovementPlaybook紐付2(), 40)


subcommand_name = sys.argv[1]
parameter_file = sys.argv[2]

with open(parameter_file) as file:
    params = yaml.load(file, Loader=yaml.CLoader)

subcommand = SubCommand()
subcommand.invoke(subcommand_name, params)
