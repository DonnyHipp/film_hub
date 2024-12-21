from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import ForeignKey, Table, Column, UniqueConstraint

from config.db import Base
from utils.db_mixins import UUIDMixin, CreatedUpdatedMixin, IDMixin
from src.models.project_models import project_members_association


if TYPE_CHECKING:
    from src.models.project_models import Project
    from src.models.rate_models import Rate


class User(UUIDMixin, CreatedUpdatedMixin, Base):
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    self_projects: Mapped["Project"] = relationship(back_populates="owner")
    projects: Mapped[list["Project"]] = relationship(
        secondary=project_members_association, back_populates="members"
    )
    birth_date: Mapped[Optional[datetime]]
    description: Mapped[Optional[str]]
    rate_from: Mapped["Rate"] = relationship(back_populates="from_user")
    rate_user: Mapped["Rate"] = relationship(back_populates="user")


user_role_association = Table(
    "user_role_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("role_id", ForeignKey("roles.id"), nullable=False),
    UniqueConstraint("user_id", "role_id", name="idx_unique_user_role"),
)


class Role(IDMixin, CreatedUpdatedMixin, Base):
    name: Mapped[str]
