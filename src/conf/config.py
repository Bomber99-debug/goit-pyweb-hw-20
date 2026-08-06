from typing import ClassVar

from src.conf.connect_settings import (
    db_host,
    db_name,
    db_password,
    db_port,
    db_user,
)


class DatabaseConfig:
    """Зберігає конфігурацію підключення до бази даних."""

    DB_URL: ClassVar[str] = (
        f"postgresql+asyncpg://"
        f"{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )


config = DatabaseConfig()