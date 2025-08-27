from typing import Any

from fastapi import Depends
from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .database import get_db
from .video_creator import VideoCreator
from .video_repository import SQLAlchemyVideoRepository

app = FastAPI()


class VideoRequest(BaseModel):
    title: str


@app.post("/video", status_code=status.HTTP_201_CREATED)
def create_video(
    video_req: VideoRequest, session: Session = Depends(get_db)
) -> dict[str, Any]:
    video_creator = VideoCreator(SQLAlchemyVideoRepository(session))
    video = video_creator.execute(video_req.title)
    return {"id": video.id, "title": video.title}
