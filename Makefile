##############################################################################
# variables

export MENU_ID ?= 2100000303

export DEBUG ?= true


# URL
export EXASTRO_PROTOCOL := http
export EXASTRO_HOST := localhost
export EXASTRO_PORT := 8080
export EXASTRO_URL := $(EXASTRO_PROTOCOL)://$(EXASTRO_HOST):$(EXASTRO_PORT)

# authentication
export EXASTRO_USERNAME := administrator
export EXASTRO_INITIAL_PASSWORD := password
export EXASTRO_PASSWORD := hogehoge
export EXASTRO_API_CREDENTIAL := $(shell echo -n "$(EXASTRO_USERNAME):$(EXASTRO_PASSWORD)" | base64)

# working dir
export WORKSPACE_DIR := $(CURDIR)/tmp

# Python configuration
export PYTHONPATH := $(CURDIR)/python-packages

# docker compose
export COMPOSE_PROJECT_NAME := shuushuu


##############################################################################
# targets

.PHONY: code-sample
code-sample:
	python3 code-sample.py


.PHONY: api-info
api-info:
	./api-info.sh


.PHONY: api-filter
api-filter:
	./api-filter.sh


.PHONY: build-exastro-container
run-exastro-container:
	$(MAKE) -C 00-exastro-container build


.PHONY: up-exastro-container
up-exastro-container:
	$(MAKE) -C 00-exastro-container up


.PHONY: down-exastro-container
down-exastro-container:
	$(MAKE) -C 00-exastro-container down


.PHONY: clean-exastro-container
clean-exastro-container:
	$(MAKE) -C 00-exastro-container clean


.PHONY: initialize-password
initialize-password:
	$(MAKE) -C 01-initialize-password initialize-password


.PHONY: administration-console
administration-console:
	$(MAKE) -C 02-administration-console administration-console


.PHONY: create-menu
create-menu:
	$(MAKE) -C 04-create-menu create-menu


.PHONY: basic-console
basic-console:
	$(MAKE) -C 06-basic-console basic-console


.PHONY: ansible-legacy-role
ansible-legacy-role:
	$(MAKE) -C 07-ansible-legacy-role ansible-legacy-role
