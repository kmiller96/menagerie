__all__ = ["app"]

from .main import app
from .auth import router

app.include_router(router, prefix="/auth", tags=["auth"])
