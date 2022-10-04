
.PHONY: unit-test
unit-test:
	@echo "== run unit tests"
	APP_ENV=unit-test poetry run pytest tests/unit

.PHONY: unit-test
smoke-test:
	@echo "== run smoke tests"
	APP_ENV=smoke-test poetry run pytest tests/smoke

.PHONY: test
test: unit-test smoke-test

.PHONY: run
run:
	@echo "== run the app"
	APP_ENV=prod python -m python_cli_skeleton_app
