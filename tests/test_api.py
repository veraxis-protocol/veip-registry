import json
import pathlib

from fastapi.testclient import TestClient
from veip_registry.app import app

client = TestClient(app)
FIXTURE = pathlib.Path(__file__).resolve().parents[0] / "fixture_pack.json"


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["ok"] is True


def test_ingest_and_fetch():
    pack = json.loads(FIXTURE.read_text(encoding="utf-8"))
    r = client.post("/v1/evidence", json=pack)
    assert r.status_code == 200
    evidence_id = r.json()["evidence_id"]

    r2 = client.get(f"/v1/evidence/{evidence_id}")
    assert r2.status_code == 200
    assert r2.json()["evidence_id"] == evidence_id
