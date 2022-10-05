# python-cli-skeleton-app

## What is it?

This is a skeleton project demonstrating how a Python CLI app can be structured.

The app does the simple task of hitting an HTTP endpoint and showing the response status code to the standard console
output.

## Driving Principles

- Use only a minimal set of Python modules that are not included in the Python Standard Library.
    - This app uses the following standard Libraries:
        - `logging` for logging
        - `configparser` for application config
        - `unittest` for unit tests
- Demonstrate testing via unit tests and smoke tests
- Demonstrate the use of modern dependency management via `Poetry`
- Illustrate environment-based application config that is suitable for deployment scenarios of the
  pattern `dev -> test -> stage -> prod`

## Stack

This Python project is laid upon the following stack:

- [Python 3.10+](https://docs.python.org/3), including the Python Standard Library
- [Poetry](https://python-poetry.org/docs/) for dependency management
- [Pytest](https://docs.pytest.org/en/7.1.x/) to organise and run tests, combined
  with [unittest](https://docs.python.org/3/library/unittest.html) to run assertions
- [requests](https://github.com/psf/requests) for HTTP calls and [responses](https://github.com/getsentry/responses) to
  mock responses in tests
- `Makefile` to orchestrate `build, test, run` cycles and standardise them across OSes

## Pre-requisites

This project assumes that the following is available on your machine:

- Python 3.6+
- `make` and `curl` executables

## How to run it

```bash

# setup tooling
# only run this once
make setup

# install/reinstall project dependencies
make install

# run the app
make run
```

You should see an output similar to the one below.

```bash
2022-10-04 16:55:53 [INFO] Using APP_ENV prod
2022-10-04 16:55:53 [INFO] Will call endpoint https://www.google.com/?q=prod
2022-10-04 16:55:53 [INFO] Endpoint URL https://www.google.com/?q=prod returned status code 200
```

## How to run tests

```bash
# all tests
make test

# unit tests only
make unit-test

# smoke tests only
make smoke-test
```

## Directory Structure

```bash
python-cli-skeleton-app
  |
  |- python_cli_skeleton_app # Business logic
  |- tests
  |   |- smoke               # Smoke tests
  |   |- unit                # Unit tests
  |- app_config.ini          # Application config to set log level, target endpoint URL, etc
  |- Makefile                # To orchestrate `build, test, run` cycles and standardise them across OSes   
  |- poetry.lock             # Ensure that exact same dependency versions are used when installing or reinstalling this project via Poetry   
  |- pyproject.toml          # Build system requirements of this Python project. Managed through Poetry in our case. See: https://python-poetry.org/docs/pyproject/
  |- README.md               # This file :)
```