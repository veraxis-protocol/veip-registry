from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .schema import validate_evidence_pack
from .storage import InMemoryStore

app = FastAPI(title="VEIP Registry (Stub)", version="0.1.0")

_store = InMemoryStore()


@app.get("/healthz")
def healthz() -> Dict[str, Any]:
    return {"ok": True}


@app.post("/v1/evidence")
def ingest_evidence(pack: Dict[str, Any]) -> Dict[str, Any]:
    # Strict schema validation
    try:
        validate_evidence_pack(pack)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"schema_invalid: {e}")

    evidence_id = pack.get("evidence_id")
    if not isinstance(evidence_id, str) or not evidence_id:
        raise HTTPException(status_code=400, detail="missing_evidence_id")

    try:
        _store.put(evidence_id, pack)
    except KeyError:
        raise HTTPException(status_code=409, detail="evidence_id_exists")

    return {"evidence_id": evidence_id}


@app.get("/v1/evidence/{evidence_id}")
def fetch_evidence(evidence_id: str) -> JSONResponse:
    try:
        pack = _store.get(evidence_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="not_found")
    return JSONResponse(content=pack)
