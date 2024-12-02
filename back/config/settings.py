import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


DB_USER: Optional[str] = os.getenv("DB_USER")
DB_PASSWORD: Optional[str] = os.getenv("DB_PASSWORD")
DB_NAME: Optional[str] = os.getenv("DB_NAME")
DB_HOST: Optional[str] = os.getenv("DB_HOST")
DB_PORT: Optional[str] = os.getenv("DB_PORT")
ENV_STATE: Optional[str] = os.getenv("ENV_STATE", "dev")

LOCAL_DB_PORT: Optional[str] = os.getenv("LOCAL_DB_PORT")

bd_port: Optional[str] = DB_PORT

if ENV_STATE == "dev":
    bd_port = LOCAL_DB_PORT


def get_main_db_url() -> str:
    return f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{bd_port}/{DB_NAME}"


