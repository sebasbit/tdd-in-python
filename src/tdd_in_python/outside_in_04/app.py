from fastapi import Depends
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .database import get_db
from .video_creator import SQLAlchemyVideoRepository
from .video_creator import VideoCreator

app = FastAPI()


class VideoRequest(BaseModel):
    title: str


@app.post("/video")
def create_video(video_req: VideoRequest, session: Session = Depends(get_db)):
    video_creator = VideoCreator(SQLAlchemyVideoRepository(session))
    video = video_creator.execute(video_req.title)
    return {"id": video.id, "title": video.title}
