
.PHONY: unit-test
unit-test:
	@echo "== run unit tests"
	APP_ENV=unit-test poetry run pytest tests/unit

.PHONY: unit-test
smoke-test:
	@echo "== run smoke tests"
	APP_ENV=smoke-test poetry run pytest tests/smoke
