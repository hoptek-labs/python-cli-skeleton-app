import requests
import logging

from python_cli_skeleton_app.app_config import AppConfig


class EndpointError(Exception):
    """
    EndpointError is raised on communication failure with the called endpoint.
    This could be due e.g. to a connection timeout.
    """
    pass


def call_endpoint():
    endpoint_url = AppConfig.get("endpoint_url")
    logging.info(f"Will call endpoint {endpoint_url}")
    try:
        response = requests.get(endpoint_url)
        return response.status_code
    except Exception:
        # Exception chaining happens automatically as we are in an except block.
        # This means that the exception trace will include both EndpointError raised below and any underlying Exception.
        # see https://docs.python.org/3/tutorial/errors.html#exception-chaining
        raise EndpointError(f"Error interacting with endpoint {endpoint_url}")
