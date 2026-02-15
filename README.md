# VEIP Registry (Stub)

Multi-operator, schema-validated intake + retrieval API for VEIP Evidence Packs.

This repository is a **minimal reference registry**. It demonstrates the external contract and safety posture for storing and serving VEIP Evidence Packs, without prescribing a single operator, vendor, or storage backend.

## What it does

- Accepts VEIP Evidence Packs via HTTP
- Validates each pack against the canonical schema (`schemas/veip-evidence-pack.schema.json`)
- Stores packs in a local in-memory store (stub)
- Serves retrieval endpoints by `evidence_id`

## What it is not

- Not the VEIP Verifier Core (conformance/certification engine)
- Not a production WORM store
- Not a supervisory endorsement system
- Not a single “global registry” assumption

## Relationship to veip-spec

- The canonical Evidence Pack schema is defined in `veip-spec/schemas/veip-evidence-pack.schema.json`
- This repo vendors that schema into `schemas/` and treats it as authoritative for validation.

## Quickstart

Python 3.10+

```bash
pip install -e ".[dev]"
make ci
make run
