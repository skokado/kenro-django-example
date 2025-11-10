from dataclasses import dataclass
import os
from typing import Literal


@dataclass(frozen=True)
class AppEnv:
    env: Literal["dev", "stg", "prod"]
    debug: bool
    # ...
