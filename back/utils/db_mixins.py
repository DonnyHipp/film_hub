import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declared_attr

from utils.utils_functions import now


class BaseMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class UUIDMixin(BaseMixin):
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)


class IDMixin(BaseMixin):
    class UUIDMixin(BaseMixin):
        id: Mapped[int] = mapped_column(primary_key=True)


class CreatedMixin(BaseMixin):
    created_at: Mapped[datetime] = mapped_column(default=now)


class UpdatedMixin(BaseMixin):
    updated_at: Mapped[datetime] = mapped_column(default=now, onupdate=now)


class CreatedUpdatedMixin(UpdatedMixin, CreatedMixin):
    pass
