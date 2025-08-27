from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class VideoRequest(BaseModel):
    title: str


@app.post("/video")
def create_video(video_req: VideoRequest):
    return
