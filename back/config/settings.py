import os
from dotenv import load_dotenv

load_dotenv()


DB_USER: str = os.getenv("DB_USER")
DB_PASSWORD: str = os.getenv("DB_PASSWORD")
DB_NAME: str = os.getenv("DB_NAME")
DB_HOST: str = os.getenv("DB_HOST")
DB_PORT: str = os.getenv("DB_PORT")
ENV_STATE: str = os.getenv("ENV_STATE", "dev")

LOCAL_DB_PORT: str = os.getenv("LOCAL_DB_PORT")

bd_port = DB_PORT

if ENV_STATE == "dev":
    bd_port = LOCAL_DB_PORT


def get_main_db_url() -> str:
    return f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{bd_port}/{DB_NAME}"


