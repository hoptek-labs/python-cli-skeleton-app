APP_MODULE=python_cli_skeleton_app

.PHONY: setup
setup:
	@echo "== setup"
	# see: https://python-poetry.org/docs/#installation
	curl -sSL "https://install.python-poetry.org" | python3 - --version 1.2.0

.PHONY: install
install:
	@echo "== install"
	poetry install

.PHONY: unit-test
unit-test:
	@echo "== run unit tests"
	APP_ENV=unit-test poetry run pytest tests/unit

.PHONY: smoke-test
smoke-test:
	@echo "== run smoke tests"
	APP_ENV=smoke-test poetry run pytest tests/smoke

.PHONY: test
test: unit-test smoke-test

.PHONY: run
run:
	@echo "== run the app"
	APP_ENV=prod python -m $(APP_MODULE)
