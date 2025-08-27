import abc

from sqlalchemy.orm import Session

from .video import Video


class VideoRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, video: Video) -> None:
        raise NotImplementedError


class SQLAlchemyVideoRepository(VideoRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, video: Video) -> None:
        self.session.add(video)
        self.session.commit()
