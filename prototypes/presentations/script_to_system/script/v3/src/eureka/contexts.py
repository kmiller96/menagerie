import sys
from contextlib import contextmanager

from loguru import logger


@contextmanager
def allow_ctrl_c():
    try:
        yield
    except KeyboardInterrupt:
        logger.info("CTRL+C received. Exiting...")
        sys.exit(0)
