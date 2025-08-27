from tdd_in_python.outside_in_04 import Video
from tdd_in_python.outside_in_04 import VideoCreator


def test_video_creator_sanitizes_title():
    title = (
        "  Title with frontend, Frontend, front-end, whitespaces, and a final dot.  "
    )
    video_creator = VideoCreator()
    video = video_creator.execute(title)
    assert (
        video.title
        == "Title with Front-end, Front-end, Front-end, whitespaces, and a final dot"
    )


def test_video_creator_saves_the_video(mocker):
    def save_side_effect(video):
        video.id = 1

    mock_repository = mocker.Mock()
    mock_repository.save.side_effect = save_side_effect

    video_creator = VideoCreator(mock_repository)
    video = video_creator.execute("Python 101")

    mock_repository.save.assert_called_once()
    assert isinstance(video, Video)
    assert video.id == 1
    assert video.title == "Python 101"
