import os

from python_cli_skeleton_app.app_config import AppConfig
from python_cli_skeleton_app.app_logger import AppLogger
from python_cli_skeleton_app.endpoint_caller import call_endpoint

logger = AppLogger.getLogger()


def run():
    try:
        logger.info(f"Using APP_ENV {os.getenv('APP_ENV')}")
        endpoint_url = AppConfig.get("endpoint_url")
        status_code = call_endpoint()
        logger.info(f"Endpoint URL {endpoint_url} returned status code {status_code}")
    except Exception as exc:
        logger.exception(exc)
        exit(1)


if __name__ == "__main__":
    run()
