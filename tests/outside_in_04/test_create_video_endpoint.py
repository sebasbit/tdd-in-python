"""
Check out Codely's repository for a full explanation:
    https://github.com/CodelyTV/refactoring-code_smells-design_patterns/tree/de397ea9e331215aa8e5c9ea4e5ff16270a9ba0f/exercises/legacy_create_video
"""

import pytest
from fastapi.testclient import TestClient

from tdd_in_python.outside_in_04 import app
from tdd_in_python.outside_in_04 import Base
from tdd_in_python.outside_in_04 import engine


@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client


def test_create_video_endpoint(client):
    response = client.post(
        "/video",
        json={"title": "  Course of frontend, Frontend, and more front-end.  "},
    )
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Course of Front-end, Front-end, and more Front-end",
    }
