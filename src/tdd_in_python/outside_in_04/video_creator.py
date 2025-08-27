import abc
import re


class Video:
    title: str


class VideoRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, video: Video):
        raise NotImplementedError


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
