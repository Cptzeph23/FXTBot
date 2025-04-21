"""system specific and performance tuning"""

from fxtbot.system.asyncio_config import asyncio_setup
from fxtbot.system.gc_setup import gc_set_threshold
from fxtbot.system.version_info import print_version_info


__all__ = ["asyncio_setup", "gc_set_threshold", "print_version_info"]
