import uuid
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, CheckConstraint


from config.db import Base
from utils.db_mixins import UUIDMixin, CreatedUpdatedMixin

if TYPE_CHECKING:
    from src.models.user_models import User


class Rate(UUIDMixin, CreatedUpdatedMixin, Base):
    score: Mapped[int] = mapped_column(CheckConstraint("score > 0 AND score <= 100"))
    from_user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    from_user: Mapped["User"] = relationship(back_populates="rate_from")
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="rate_user")
