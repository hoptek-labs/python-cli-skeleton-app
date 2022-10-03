import os
from unittest import TestCase, mock


class TestAppConfig(TestCase):

    # Taken from https://adamj.eu/tech/2020/10/13/how-to-mock-environment-variables-with-pythons-unittest/
    @mock.patch.dict(os.environ, {}, clear=True)
    def test_raises_error_when_app_env_not_set(self):
        with self.assertRaises(RuntimeError) as error:
            # the line below should raise an error
            from python_cli_skeleton_app.app_config import AppConfig
            # this call should not happen
            AppConfig.get("should-not-get-to-this-line")
        self.assertEqual(
            "Missing environment variable APP_ENV",
            str(error.exception)
        )

    def test_returns_expected_string_value(self):
        from python_cli_skeleton_app.app_config import AppConfig
        actual_test_value = AppConfig.get("test_key_string")
        self.assertEqual("test_value_string", actual_test_value)

    def test_returns_expected_int_value(self):
        from python_cli_skeleton_app.app_config import AppConfig
        actual_test_value = AppConfig.getint("test_key_int")
        self.assertEqual(42, actual_test_value)