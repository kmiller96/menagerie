import os

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
URL = f"http://localhost:8000?debug={str(DEBUG).lower()}"
