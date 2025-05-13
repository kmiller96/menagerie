import os

PACKAGE_PATH, _ = os.path.split(__file__)
USER_HUB_PATH = os.path.join(
    os.path.expanduser('~'),
    '.hub'
)