import configparser
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

    app_env = os.getenv("APP_ENV")
    if app_env is None:
        raise RuntimeError("Missing environment variable APP_ENV")

    if app_env not in config.sections():
        raise RuntimeError(
            f"{app_config_filename} does not contain a section for APP_ENV {app_env}"
        )

    @staticmethod
    def get(key):
        return AppConfig.config.get(AppConfig.app_env, key)

    @staticmethod
    def getint(key):
        return AppConfig.config.getint(AppConfig.app_env, key)
