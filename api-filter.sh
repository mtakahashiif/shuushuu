#!/bin/bash

MENU_ID=${MENU_ID:-2100000303}

curl \
    --request POST \
    --header "Host: ${EXASTRO_HOST}:${EXASTRO_PORT}" \
    --header "Authorization: ${EXASTRO_API_CREDENTIAL}" \
    --header 'X-Command: FILTER' \
    ${EXASTRO_URL}'/default/menu/07_rest_api_ver1.php?no='${MENU_ID} | jq
