
import os
from CONFIG._config import Config as BaseConfig


def env_int(name, default):
    value = os.getenv(name)
    return int(value) if value not in (None, "") else default


def env_list(name, default=None):
    value = os.getenv(name)
    if value is None:
        return default if default is not None else []
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def required_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required Render environment variable: {name}")
    return value


class Config(BaseConfig):
    BOT_NAME = os.getenv("BOT_NAME", BaseConfig.BOT_NAME)
    BOT_NAME_FOR_USERS = os.getenv(
        "BOT_NAME_FOR_USERS", BaseConfig.BOT_NAME_FOR_USERS
    )

    ADMIN = env_list("ADMIN", [])
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "@")

    ADMIN_GROUP = env_list("ADMIN_GROUP", [])
    ALLOWED_GROUP = env_list("ALLOWED_GROUP", [])
    ALLOWED_USERS = env_list("ALLOWED_USERS", ADMIN)

    API_ID = int(required_env("API_ID"))
    API_HASH = required_env("API_HASH")
    BOT_TOKEN = required_env("BOT_TOKEN")

    LOGS_ID = env_int("LOGS_ID", ADMIN[0] if ADMIN else 0)
    LOGS_VIDEO_ID = env_int(
        "LOGS_VIDEO_ID", LOGS_ID
    )
    LOGS_NSFW_ID = env_int(
        "LOGS_NSFW_ID", LOGS_ID
    )
    LOGS_IMG_ID = env_int(
        "LOGS_IMG_ID", LOGS_ID
    )
    LOGS_PAID_ID = env_int(
        "LOGS_PAID_ID", LOGS_ID
    )
    LOG_EXCEPTION = env_int(
        "LOG_EXCEPTION", LOGS_ID
    )

    SUBSCRIBE_CHANNEL = env_int("SUBSCRIBE_CHANNEL", 0)
    SUBSCRIBE_CHANNEL_URL = os.getenv("SUBSCRIBE_CHANNEL_URL", "")

    USE_FIREBASE = os.getenv(
        "USE_FIREBASE", "false"
    ).lower() in ("1", "true", "yes")

    BOT_DB_PATH = f"bot/{BOT_NAME_FOR_USERS}/"
