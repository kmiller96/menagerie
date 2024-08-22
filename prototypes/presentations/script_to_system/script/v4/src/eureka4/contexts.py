import signal
import sys
from contextlib import contextmanager

from loguru import logger


@contextmanager
def allow_sigterm():
    def handler(*_):
        logger.info("SIGTERM received. Exiting...")
        sys.exit(0)

    signal.signal(
        signal.SIGTERM,
        lambda *_: handler,
    )

    yield
