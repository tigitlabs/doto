.DEFAULT_GOAL:=help
SHELL:=/bin/bash

# --------------------------
.PHONY: help
help:       	## Show this help.
	@echo "Convinient make targets for development and testing"
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Github Actions - ACT

.PHONY: github-action-list
github-action-list:	## ✅List Workflows
	@echo "📋 List Push Workflows"
	@act push --list
	@echo "📋 List Pull Request Workflows"
	@act pull_request --list

.PHONY: github-action-ci
github-action-act-test:	## ✅Run act-test
	act -W .github/workflows/ci.yml

##@ 🧪 Tests and Checks

.PHONY: ci-yamllint
ci-yamllint:	## 🏃‍♂️ Run yamllint
	@echo "🧪 yamllint"
	@yamllint .

.PHONY: ci-molecule-test
ci-molecule-test:	## 🏃‍♂️ Run molecule
	@echo "🧪 molecule"
	@cd ansible/ && \
	molecule test && \
	cd ..

.PHONY: ci-molecule-converge
ci-molecule-converge:	## 🏃‍♂️ Run molecule converge
	@echo "🧪 molecule converge"
	@cd ansible/ && \
	molecule converge && \
	cd ..

.PHONY: ci-run-in-docker
ci-run-in-docker:	## 🏃‍♂️ Run in Docker
	@echo "🧪 Run in Docker"
	@echo "🔨 Build Docker Image"
	@docker build --tag doto/ubuntu2204:latest --file ansible/molecule/Docker/Dockerfile ansible/molecule/Docker/
	@echo "🗑️ Remove old container"
	@docker rm --force doto-ubuntu2204 || true
	@echo "🏃‍♂️ Run Docker Container"
	@docker run \
	--name=doto-ubuntu2204 \
	--user ubuntu \
	--detach \
	--privileged \
	--volume=/sys/fs/cgroup:/sys/fs/cgroup:rw \
	--volume=`pwd`:/etc/ansible/roles/role_under_test:ro \
	--cgroupns=host \
	doto/ubuntu2204:latest

.PHONY: ci-all
ci-all:	## 🧪 Run all makefile targets
	@make ci-yamllint
