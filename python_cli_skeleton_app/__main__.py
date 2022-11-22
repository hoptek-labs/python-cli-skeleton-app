import os

from python_cli_skeleton_app.app_config import AppConfig
from python_cli_skeleton_app.app_logger import AppLogger
from python_cli_skeleton_app.endpoint_caller import call_endpoint

logger = AppLogger.get_logger()


def run():
    try:
        logger.info(f"Using APP_ENV {os.getenv('APP_ENV')}")
        endpoint_url = AppConfig.get("endpoint_url")
        status_code, response_body = call_endpoint()
        logger.info(f"Endpoint URL {endpoint_url} returned status code {status_code}")
        logger.info(f"Endpoint URL {endpoint_url} returned response body {response_body}")
    except Exception as exc:
        logger.exception(exc)
        exit(1)


if __name__ == "__main__":
    run()
