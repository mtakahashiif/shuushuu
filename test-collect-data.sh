#!/bin/bash

BASE_DIR=$(cd $(dirname $0); pwd)
ansible-playbook test-collect-data.yml --extra-vars "__parameter_dir__=${BASE_DIR} inventory_hostname=tmp"
