from .base import *  # noqa
from .types import AppEnv


ALLOWED_HOSTS = ["*"]


APP_ENV = AppEnv(
    env="dev",
    debug=True,
)

# ...
