from sqlalchemy.orm import Mapped

from config.db import Base
from utils.db_mixins import UUIDMixin, CreatedUpdatedMixin


class User(UUIDMixin, CreatedUpdatedMixin, Base):
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]

