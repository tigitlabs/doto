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


.PHONY: ci-all
ci-all:	## 🧪 Run all makefile targets
	@make ci-yamllint
