from tdd_in_python.outside_in_04 import VideoCreator


def test_video_creator_removes_trailing_and_leading_spaces():
    title = "  title with spaces  "
    video_creator = VideoCreator()
    video = video_creator.execute(title)
    assert video.title == "title with spaces"
