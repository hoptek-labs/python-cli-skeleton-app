import os
import sys
from unittest import TestCase, mock

from python_cli_skeleton_app.app_config import AppConfig


def remove_module_from_imports(module_name):
    if module_name in sys.modules:
        del sys.modules[module_name]


class TestAppConfig(TestCase):

    # Taken from https://adamj.eu/tech/2020/10/13/how-to-mock-environment-variables-with-pythons-unittest/
    @mock.patch.dict(os.environ, {}, clear=True)
    def test_raises_error_when_app_env_not_set(self):
        with self.assertRaises(RuntimeError) as error:
            # ensure that AppConfig will be reloaded on import so that we can test an error being raised
            remove_module_from_imports('python_cli_skeleton_app.app_config')
            # the line below should raise an error
            from python_cli_skeleton_app.app_config import AppConfig
            # this call should not happen
            AppConfig.get("should-not-get-to-this-line")
        self.assertEqual(
            "Missing environment variable APP_ENV",
            str(error.exception)
        )

    @mock.patch.dict(os.environ, {"APP_ENV": "invalid_app_env"})
    def test_raises_error_when_no_section_corresponding_to_app_env(self):
        with self.assertRaises(RuntimeError) as error:
            # ensure that AppConfig will be reloaded on import so that we can test an error being raised
            remove_module_from_imports('python_cli_skeleton_app.app_config')
            # the line below should raise an error
            from python_cli_skeleton_app.app_config import AppConfig
            # this call should not happen
            AppConfig.get("should-not-get-to-this-line")
        self.assertEqual(
            f"app_config.ini does not contain a section for APP_ENV invalid_app_env",
            str(error.exception)
        )

    def test_returns_expected_string_value(self):
        actual_test_value = AppConfig.get("test_key_string")
        self.assertEqual("test_value_string", actual_test_value)

    def test_returns_expected_int_value(self):
        actual_test_value = AppConfig.getint("test_key_int")
        self.assertEqual(42, actual_test_value)
