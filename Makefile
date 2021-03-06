.DEFAULT_GOAL := help

PROJECT_NAME = jwt_service
CONTAINER_NAME = jwt_container

install: ## Install all project
	@echo 'Installing the project'
	@make build
	@make up
	@echo 'for more details use: make logs'

uninstall: ## Remove all project
	@echo 'Deleting the project'
	@make down
	@echo 'Project deleted'

build: ## build IMAGE, use me with: make build
	@docker-compose -f docker-compose.build.yml build

up: ## up docker containers
	docker-compose -p $(PROJECT_NAME) up -d
	@echo 'Container status'
	docker-compose -p $(PROJECT_NAME) ps

stop: ## Stop and remove the docker containers, use me with: make down
	docker-compose -p $(PROJECT_NAME) stop

down: ## Stop and remove the docker containers, use me with: make down
	docker-compose -p $(PROJECT_NAME) down

restart: ## Restart all containers, use me with: make restart
	docker-compose -p $(PROJECT_NAME) restart
	docker-compose -p $(PROJECT_NAME) ps

status: ## Show containers status, use me with: make status
	docker-compose -p $(PROJECT_NAME) ps

ssh: ## Connect to container for ssh protocol
	docker exec -it $(CONTAINER_NAME) bash

logs: ## Show docker logs
	docker logs $(CONTAINER_NAME) -f

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
