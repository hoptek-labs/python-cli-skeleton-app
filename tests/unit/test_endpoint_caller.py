from unittest import TestCase, mock

from requests.exceptions import Timeout

from python_cli_skeleton_app.app_config import AppConfig
from python_cli_skeleton_app.endpoint_caller import call_endpoint, EndpointError


class TestEndpointCaller(TestCase):

    # see examples of the patch decorator here: https://realpython.com/python-mock-library/
    @mock.patch('python_cli_skeleton_app.endpoint_caller.requests')
    def test_raises_error_on_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(EndpointError) as error:
            call_endpoint()
        self.assertEqual(
            f"Error interacting with endpoint {AppConfig.get('endpoint_url')}",
            str(error.exception)
        )
