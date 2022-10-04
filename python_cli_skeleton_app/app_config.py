import configparser
import logging
import os
from pathlib import Path

app_config_filename = "app_config.ini"


class AppConfig:
    """
    This class stores app configuration, as loaded from the top-level app_config.ini
    """
    config = configparser.ConfigParser()

    # unfortunately, this class needs to hard-codedly know the location of the application configuration file
    root_dir = Path(__file__).parent.parent
    config.read(f"{root_dir}/{app_config_filename}")

    section = os.getenv('APP_ENV')
    if section is None:
        raise RuntimeError("Missing environment variable APP_ENV")

    logging.info(f"Using APP_ENV {section}")

    @staticmethod
    def get(key):
        return AppConfig.config.get(AppConfig.section, key)

    @staticmethod
    def getint(key):
        return AppConfig.config.getint(AppConfig.section, key)
