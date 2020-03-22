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


def test_hello_world(client):
    rv = client.get("/")
    assert rv.data == b"hello world!"
