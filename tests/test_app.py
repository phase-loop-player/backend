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


def test_root_route_no_query_string(client):
    rv = client.get("/api/regions")
    assert rv.status_code == 400


def test_root_route(client):
    path = "/api/regions?url=https://www.youtube.com/watch?v=gGVD8vzWWmU&t=1s"
    rv = client.get(path)
    assert rv.status_code == 200
