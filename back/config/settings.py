import os
from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: int
    local_db_port: str
    env_state: Optional[str] = Field("dev")

    class Config:
        env_file = os.path.join(BASE_DIR.parent, ".env")
        case_sensitive = False

    @property
    def effective_db_port(self) -> str:
        return self.local_db_port if self.env_state == "dev" else self.db_port

    def get_main_db_url(self, mode: str = "+asyncpg") -> str:
        return f"postgresql{mode}://{self.db_user}:{self.db_password}@{self.db_host}:{self.effective_db_port}/{self.db_name}"

    def get_sync_db_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.effective_db_port}/{self.db_name}"


settings = Settings()
