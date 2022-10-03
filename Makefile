
.PHONY: unit-test
unit-test:
	@echo "== run unit tests"
	APP_ENV=unit-test poetry run pytest tests/unit
