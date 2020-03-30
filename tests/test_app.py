# pylint: disable=redefined-outer-name

import pytest
from auditok_server.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    rv = client.get("/healthz")
    assert rv.status_code == 204


def test__no_query_string(client):
    rv = client.get("/api/regions")
    assert rv.status_code == 400


def test_regions_api(client):
    path = (
        "/api/regions?url=https://www.youtube.com/watch?"
        + "v=gGVD8vzWWmU&t=1s&min_duration=10&max_duration=20"
    )
    rv = client.get(path)
    expected = (
        '{"regions":[{"end":149.1,"start":133.75},'
        + '{"end":185.85902083333335,"start":172.20000000000002}]}\n'
    )
    assert rv.status_code == 200
    assert rv.data == bytes(expected, encoding="utf-8")
