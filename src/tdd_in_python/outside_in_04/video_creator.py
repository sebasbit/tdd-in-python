import abc
import re

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session

from .database import Base


class Video(Base):
    __tablename__ = "videos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]


class VideoRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, video: Video):
        raise NotImplementedError


class SQLAlchemyVideoRepository(VideoRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, video: Video):
        self.session.add(video)
        self.session.commit()


class VideoCreator:
    def __init__(self, video_repository: VideoRepository):
        self.video_repository = video_repository

    def execute(self, title: str):
        video = Video()
        video.title = self.sanitize_title(title)
        self.video_repository.save(video)
        return video

    def sanitize_title(self, title: str) -> str:
        pattern = r"frontend|Frontend|front-end"
        replacement = "Front-end"
        return re.sub(pattern, replacement, title).strip().rstrip(".")
