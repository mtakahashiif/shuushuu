#!/bin/bash -x

##############################################################################
# variables

EXASTRO_COOKIE_FILE=${WORKSPACE_DIR}/initialize-password-cookie.txt


##############################################################################
# URL encoding (username/password)

function urlencode() {
    python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1]))" "${1}"
}

EXASTRO_URL_ENCODED_USERNAME=$(urlencode ${EXASTRO_USERNAME})
EXASTRO_URL_ENCODED_INITIAL_PASSWORD=$(urlencode ${EXASTRO_INITIAL_PASSWORD})
EXASTRO_URL_ENCODED_PASSWORD=$(urlencode ${EXASTRO_PASSWORD})


##############################################################################
# initialize password

rm ${EXASTRO_COOKIE_FILE}

curl \
    --request GET \
    --location \
    --cookie-jar ${EXASTRO_COOKIE_FILE} \
    ${EXASTRO_URL}'/common/common_auth.php?login&grp=&no='

curl \
    --request POST \
    --location \
    --cookie ${EXASTRO_COOKIE_FILE} \
    --cookie-jar ${EXASTRO_COOKIE_FILE} \
    --header 'Referer: '${EXASTRO_URL}'/common/common_auth.php?login&grp=&no=' \
    --data 'username='${EXASTRO_URL_ENCODED_USERNAME}'&password='${EXASTRO_URL_ENCODED_PASSWORD}'&login=%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3' \
    ${EXASTRO_URL}'/common/common_auth.php?login&grp=0000000000&no='

curl \
    --request POST \
    --location \
    --cookie ${EXASTRO_COOKIE_FILE} \
    --cookie-jar ${EXASTRO_COOKIE_FILE} \
    --header 'Referer: '${EXASTRO_URL}'/default/mainmenu/01_browse.php?grp=0000000000' \
    --data 'expiry=0&username='${EXASTRO_URL_ENCODED_USERNAME} \
    ${EXASTRO_URL}'/common/common_change_password_form.php?login&grp=0000000000&no='
    
curl \
    --request POST \
    --location \
    --cookie ${EXASTRO_COOKIE_FILE} \
    --cookie-jar ${EXASTRO_COOKIE_FILE} \
    --header 'Referer: '${EXASTRO_URL}'/common/common_change_password_form.php?login&grp=0000000000&no=\r\n' \
    --data 'old_password='${EXASTRO_URL_ENCODED_INITIAL_PASSWORD}'&new_password='${EXASTRO_URL_ENCODED_PASSWORD}'&new_password_2='${EXASTRO_URL_ENCODED_PASSWORD}'&submit=%E5%A4%89%E6%9B%B4&expiry=0' \
    ${EXASTRO_URL}'/common/common_change_password_do.php?grp=0000000000&no='


##############################################################################
# test

curl \
    --request POST \
    --header "Host: ${EXASTRO_HOST}:${EXASTRO_PORT}" \
    --header "Authorization: ${EXASTRO_API_CREDENTIAL}" \
    --header 'X-Command: INFO' \
    ${EXASTRO_URL}'/default/menu/07_rest_api_ver1.php?no=2100000303' | jq
