#!/bin/bash -x

##############################################################################
# create zipped role

cp -R roles ${WORKSPACE_DIR}
python3 create-collected-data.py > ${WORKSPACE_DIR}/roles/data_collector/files/collected-data.yml
(cd ${WORKSPACE_DIR} && zip ${WORKSPACE_DIR}/upload-file.zip -r roles)


##############################################################################
# invoke API

python3 ansible-legacy-role.py
