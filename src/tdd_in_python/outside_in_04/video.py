from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .database import Base


class Video(Base):  # type: ignore[misc]
    __tablename__ = "videos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
