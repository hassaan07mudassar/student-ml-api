import json

import pytest

import app as app_module
from app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
    "status": "healthy",
    "application": "student-ml-api",
    "application_version": "1.1.0",
    "model_version": "model-1",
}


def test_successful_prediction(client):
    response = client.post("/predict", json={"value": 10})

    assert response.status_code == 200
    assert response.get_json() == {"input": 10, "prediction": 20}


def test_missing_input(client):
    response = client.post("/predict", json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "missing required field: value"}


def test_invalid_input(client):
    response = client.post("/predict", json={"value": "ten"})

    assert response.status_code == 400
    assert response.get_json() == {"error": "value must be a number"}


def test_malformed_json(client):
    response = client.post(
        "/predict",
        data="{not-json}",
        content_type="application/json",
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "request body must be valid JSON"}


def test_health_endpoint_v1_1_includes_model_metadata(client, monkeypatch):
    monkeypatch.setattr(app_module, "read_version", lambda: "1.1.0")

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
    assert response.get_json() == {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": "1.1.0",
        "model_version": "model-1",
    }
