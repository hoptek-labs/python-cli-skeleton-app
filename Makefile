APP_MODULE=python_cli_skeleton_app

.PHONY: setup
setup:
	@echo "== setup"
	# see: https://python-poetry.org/docs/#installation
	curl -sSL "https://install.python-poetry.org" | python3 - --version 1.2.2

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

.PHONY: clean
clean:
	@echo "== clean"
	find . -depth -type d -name '__pycache__' -exec rm -rf '{}' \;

.PHONY: lint-check
lint-check:
	@echo "== run lint"
	@echo "\n\n== run mypy"
	poetry run mypy $(APP_MODULE) tests
	@echo "\n\n== run isort"
	poetry run isort --check $(APP_MODULE) tests
	@echo "\n\n== run black"
	poetry run black --check $(APP_MODULE) tests
	@echo "\n\n== run flake8"
	poetry run flake8 $(APP_MODULE) tests

.PHONY: lint
lint:
	@echo "== run lint"
	@echo "\n\n== run mypy"
	poetry run mypy $(APP_MODULE) tests
	@echo "\n\n== run isort"
	poetry run isort $(APP_MODULE) tests
	@echo "\n\n== run black"
	poetry run black $(APP_MODULE) tests
	@echo "\n\n== run flake8"
	poetry run flake8 $(APP_MODULE) tests

.PHONY: run
run:
	@echo "== run the app"
	APP_ENV=prod python -m $(APP_MODULE)

