import pytest

from tdd_in_python.outside_in_04 import Video
from tdd_in_python.outside_in_04 import VideoCreator


@pytest.fixture()
def mock_repository(mocker):
    def save_side_effect(video):
        video.id = 1

    mock_repository = mocker.Mock()
    mock_repository.save.side_effect = save_side_effect
    yield mock_repository
    mock_repository.save.assert_called_once()


def test_video_creator(mock_repository):
    title = (
        "  Title with frontend, Frontend, front-end, whitespaces, and a final dot.  "
    )
    expected_title = (
        "Title with Front-end, Front-end, Front-end, whitespaces, and a final dot"
    )

    video_creator = VideoCreator(mock_repository)
    video = video_creator.execute(title)

    assert isinstance(video, Video)
    assert isinstance(video.id, int)
    assert video.title == expected_title
