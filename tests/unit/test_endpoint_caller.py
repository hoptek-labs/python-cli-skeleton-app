from unittest import TestCase, mock

import responses
from requests.exceptions import Timeout

from python_cli_skeleton_app.app_config import AppConfig
from python_cli_skeleton_app.endpoint_caller import EndpointError, call_endpoint


class TestEndpointCaller(TestCase):

    # see examples of the patch decorator here: https://realpython.com/python-mock-library/
    @mock.patch("python_cli_skeleton_app.endpoint_caller.requests")
    def test_raises_error_on_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(EndpointError) as error:
            call_endpoint()
        self.assertEqual(
            str(error.exception),
            f"Error interacting with endpoint {AppConfig.get('endpoint_url')}",
        )

    @responses.activate
    def test_returns_status_code(self):
        endpoint_url = AppConfig.get("endpoint_url")
        for status_code in [200, 400, 404, 500]:
            with self.subTest(msg=f"Returns status code {status_code}"):
                responses.add(
                    responses.GET,
                    endpoint_url,
                    body="some response body",
                    status=status_code,
                )

                self.assertEqual(call_endpoint(), status_code)
