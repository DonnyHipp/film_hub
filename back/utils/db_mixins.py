import uuid
from datetime import datetime


from sqlalchemy.orm import Mapped, mapped_column

from utils.utils_functions import now


class UUIDMixin:
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)


class IDMixin:
    id: Mapped[int] = mapped_column(primary_key=True)


class CreatedMixin:
    created_at: Mapped[datetime] = mapped_column(default=now)


class UpdatedMixin:
    updated_at: Mapped[datetime] = mapped_column(default=now, onupdate=now)


class CreatedUpdatedMixin(UpdatedMixin, CreatedMixin):
    pass
