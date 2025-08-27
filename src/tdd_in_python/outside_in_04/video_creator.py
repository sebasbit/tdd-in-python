import re


class Video:
    title: str


class VideoCreator:
    def execute(self, title: str):
        video = Video()
        title = re.sub(r"frontend|Frontend|front-end", "Front-end", title)
        video.title = title.strip().rstrip(".")
        return video
