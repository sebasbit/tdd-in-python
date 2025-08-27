class Video:
    title: str


class VideoCreator:
    def execute(self, title: str):
        video = Video()
        video.title = title.strip()
        return video
