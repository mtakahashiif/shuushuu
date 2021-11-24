.PHONY: build
build:
	docker-compose build


.PHONY: up
up:
	docker-compose up -d


.PHONY: down
down:
	docker-compose down


.PHONY: clean
clean: clean
	docker system prune --force
	docker volume prune --force
