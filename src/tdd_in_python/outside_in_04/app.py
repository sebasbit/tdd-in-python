from fastapi import FastAPI
from pydantic import BaseModel

from .video_creator import VideoCreator

app = FastAPI()


class VideoRequest(BaseModel):
    title: str


@app.post("/video")
def create_video(video_req: VideoRequest):
    video_creator = VideoCreator()
    video = video_creator.execute(video_req.title)
    return {"id": video.id, "title": video.title}
