"""Start-up smoke test: the model loads, the form is served and /predict returns a rating."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import api  # noqa: E402

SAMPLE = {
    "startYear": "2024",
    "runtimeMinutes": "120",
    "budget": "5000000",
    "Language": "English",
    "Country": "USA",
    "actor_1": '["nm0000138","nm0000701"]',
    "writer_1": '["nm0000116"]',
    "genre_1": '["Action","Drama"]',
}


def test_model_loads():
    assert api.model is not None


def test_home_page():
    resp = api.app.test_client().get("/")
    assert resp.status_code == 200
    assert b"predictForm" in resp.data


def test_predict_returns_rating():
    resp = api.app.test_client().post("/predict", json=SAMPLE)
    assert resp.status_code == 200, resp.get_json()
    rating = resp.get_json()["predicted_rating"]
    assert isinstance(rating, (int, float))
    assert 0 <= rating <= 10


def test_predict_rejects_missing_fields():
    resp = api.app.test_client().post("/predict", json={"startYear": "2024"})
    assert resp.status_code == 400
