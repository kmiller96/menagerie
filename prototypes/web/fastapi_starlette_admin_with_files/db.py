"""Initialises the DB."""

from sqlmodel import SQLModel

from app import engine, User  # noqa: F401

SQLModel.metadata.create_all(engine)
