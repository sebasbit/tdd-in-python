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
