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


.PHONY: build-exastro
run-exastro:
	$(MAKE) -C 00-exastro-container build


.PHONY: up-exastro
up-exastro:
	$(MAKE) -C 00-exastro-container up


.PHONY: down-exastro
down-exastro:
	$(MAKE) -C 00-exastro-container down


.PHONY: clean-exastro
clean-exastro:
	$(MAKE) -C 00-exastro-container clean


.PHONY: init-password
init-password:
	./init-password.sh


.PHONY: enable-menu
enable-menu:
	python3 -m shuushuu enable_menu $(CURDIR)/params.yml


.PHONY: create-menu-items
create-menu-items:
	python3 -m shuushuu create_menu_items $(CURDIR)/params.yml


.PHONY: create-movement
create-movement:
	python3 -m shuushuu create_movement $(CURDIR)/params.yml


.PHONY: create-role-package
create-role-package:
	python3 -m shuushuu create_role_package $(CURDIR)/params.yml
