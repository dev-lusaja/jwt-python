.DEFAULT_GOAL := help

TAG_BACKEND = latest
IMAGE_NAME = jwt-services
PROJECT_NAME = jwtservice
CONTAINER_NAME = jwtservice_backend
REGISTRY_HOST = local.urbania.registry:5000

pull: ## pull docker images from Cesar Registery, use me with: make pull
	docker pull $(REGISTRY_HOST)/$(IMAGE_NAME):$(TAG_BACKEND)
	docker tag $(REGISTRY_HOST)/$(IMAGE_NAME):$(TAG_BACKEND) $(IMAGE_NAME):$(TAG_BACKEND)
	docker rmi $(REGISTRY_HOST)/$(IMAGE_NAME):$(TAG_BACKEND)
	docker images

push: ## pull docker images from Cesar Registry, use me with: make pull
	docker tag $(IMAGE_NAME):$(TAG_BACKEND) $(REGISTRY_HOST)/$(IMAGE_NAME):$(TAG_BACKEND)
	docker push $(REGISTRY_HOST)/$(IMAGE_NAME):$(TAG_BACKEND)
	docker rmi $(REGISTRY_HOST)/$(IMAGE_NAME):$(TAG_BACKEND)
	docker images

build: ## build IMAGE, use me with: make build
	@docker-compose -f docker-compose.build.yml build --no-cache

up: ## up docker containers
	docker-compose -p $(PROJECT_NAME) up -d
	docker-compose -p $(PROJECT_NAME) ps

stop: ## Stops and removes the docker containers, use me with: make down
	docker-compose -p $(PROJECT_NAME) stop

down: ## Stops and removes the docker containers, use me with: make down
	docker-compose -p $(PROJECT_NAME) down

restart: ## Restart all containers, use me with: make restart
	docker-compose -p $(PROJECT_NAME) restart
	docker-compose -p $(PROJECT_NAME) ps

status: ## Show containers status, use me with: make status
	docker-compose -p $(PROJECT_NAME) ps

ssh: ## Connect to container for ssh protocol
	docker exec -it $(CONTAINER_NAME) bash

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
