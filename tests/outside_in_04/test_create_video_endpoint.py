import pytest
from fastapi.testclient import TestClient

from tdd_in_python.outside_in_04 import app


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client


def test_create_video_endpoint(client):
    response = client.post(
        "/video", data={"title": "  Course of frontend, Frontend,and more front-end.  "}
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Course of Front-End, Front-End, and more Front-End",
    }
