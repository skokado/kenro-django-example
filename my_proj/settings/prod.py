from .base import *  # noqa
from .types import AppEnv


ALLOWED_HOSTS = ["example.com"]

APP_ENV = AppEnv(
    env="prod",
    debug=False,
)

# ...
