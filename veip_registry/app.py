# veip_registry/app.py
from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .schema import validate_evidence_pack
from .storage import InMemoryStore

app = FastAPI(
    title="VEIP Registry (Stub)",
    version="0.1.0",
    description="Schema-validated intake + retrieval API for VEIP Evidence Packs (reference stub).",
)

_store = InMemoryStore()


@app.get("/")
def root() -> dict:
    return {"name": "veip-registry", "status": "ok", "version": "0.1.0"}


@app.get("/healthz")
def healthz() -> dict:
    return {"ok": True}


@app.post("/v1/evidence")
def ingest_evidence(pack: dict) -> JSONResponse:
    """
    Ingest a VEIP Evidence Pack (JSON object), validate against the vendored schema,
    and store by evidence_id.
    """
    try:
        validate_evidence_pack(pack)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Schema validation failed: {e}")

    evidence_id = pack.get("evidence_id")
    if not isinstance(evidence_id, str) or not evidence_id:
        # Schema should enforce, but keep an explicit guard.
        raise HTTPException(status_code=400, detail="Missing or invalid evidence_id")

    _store.put(evidence_id, pack)
    return JSONResponse({"ok": True, "evidence_id": evidence_id})


@app.get("/v1/evidence/{evidence_id}")
def fetch_evidence(evidence_id: str) -> JSONResponse:
    pack = _store.get(evidence_id)
    if pack is None:
        raise HTTPException(status_code=404, detail="Not found")
    return JSONResponse(pack)


def main() -> None:
    import uvicorn

    uvicorn.run("veip_registry.app:app", host="127.0.0.1", port=8080, reload=False)


if __name__ == "__main__":
    main()
