.PHONY: build
build:
	DOCKER_BUILDKIT=1 docker build \
		--tag centos8-with-ssh-server:1.0.0 \
		--no-cache \
		--build-arg HTTP_PROXY \
		--build-arg http_proxy \
		--build-arg HTTPS_PROXY \
		--build-arg https_proxy \
		--build-arg NO_PROXY \
		--build-arg no_proxy \
		$(DOCKER_BUILD_OPT_SECRET) \
		centos8-with-ssh-server


.PHONY: up
up:
	docker-compose up -d


.PHONY: down
down:
	docker-compose down


.PHONY: clean
clean:
	docker system prune --force
	docker volume prune --force
