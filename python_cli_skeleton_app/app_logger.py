import logging
import sys

from python_cli_skeleton_app.app_config import AppConfig


class AppLogger:
    """
    AppLogger configures a logger for the app and provides a single logger instance.
    """
    logger = logging.getLogger()
    logging.basicConfig(
        stream=sys.stdout,
        encoding="utf-8",
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(asctime)s [%(levelname)s] %(message)s",
        level=AppConfig.get("log_level")
    )

    @staticmethod
    def getLogger():
        return AppLogger.logger
