from typing import TYPE_CHECKING, Optional, List

from sqlalchemy import ForeignKey, Table, Column, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config.db import Base
from utils.db_mixins import UUIDMixin, CreatedUpdatedMixin, IDMixin

if TYPE_CHECKING:
    from src.models.user_models import User


project_members_association = Table(
    "project_user_association",
    Base.metadata,
    Column("project_id", ForeignKey("projects.id"), nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable=False),
    UniqueConstraint("project_id", "user_id", name="idx_unique_project_user"),
)


class ProjectStatus(IDMixin, Base):
    __tablename__ = "project_statuses"

    name: Mapped[str]
    projects: Mapped[List["ProjectStatus"]] = relationship(back_populates="status")


class Project(UUIDMixin, CreatedUpdatedMixin, Base):
    name: Mapped[str] = mapped_column(unique=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="self_projects")
    members: Mapped[list["User"]] = relationship(
        secondary=project_members_association, back_populates="projects"
    )
    status_id: Mapped[Optional[int]] = mapped_column(ForeignKey("project_statuses.id"))
    status: Mapped["ProjectStatus"] = relationship(back_populates="projects")
