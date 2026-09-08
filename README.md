# VEIP Registry (Reference Implementation)

Multi-operator, schema-validated intake and retrieval API for VEIP Evidence Packs.

This repository provides a minimal, vendor-neutral reference registry for storing and serving VEIP Evidence Packs. It demonstrates the external contract and safety posture expected of a VEIP-compatible registry implementation.

It is intentionally compact and transparent.

---

## Role in Open Institutional Computation

**Category:** Open Institutional Computation  
**This component:** Reference intake and retrieval surface for VEIP Evidence Packs — storage and service of evidence state  
**VEIP — Veraxis Execution Integrity Protocol:** the execution-integrity and interoperability boundary that binds already-established machine-operational authority/control state to an exact action and runtime disposition, and emits the Evidence Packs this registry stores. VEIP does not interpret governing documents, perform institutional admission, or originate institutional authority.  
**Upstream:** Evidence Packs emitted by VEIP implementations, themselves downstream of machine-operational authority/control state established through authorized institutional interpretation and admission (the Veraxis reference path for that upstream problem is [OIC — Open Institutional Compiler](https://github.com/veraxis-protocol/Institutional-Compiler))  
**Downstream:** Retrieval by verifiers, examiners and reconciliation processes  
**Canonical category thesis:** https://github.com/veraxis-protocol/institutional-continuity/blob/main/THESIS.md

A registry stores/serves evidence state. It does not originate the institutional authority represented by that state.

This is why the boundaries stated below matter: a registry that accepted, stored and served a pack perfectly has established custody of evidence, not the legitimacy of the authority that evidence describes.

Architectural role does not imply production readiness; see "What This Repository Is Not" below for the exact demonstrated scope.

---

## Purpose

The VEIP Registry defines the **external intake and retrieval surface** for Evidence Packs.

It enforces:

- Canonical schema validation
- Deterministic ingestion semantics
- Evidence retrieval by `evidence_id`
- Clear separation from conformance or certification logic

This repository demonstrates those invariants in a minimal FastAPI implementation.

---

## What This Repository Does

- Accepts VEIP Evidence Packs via HTTP (`POST /v1/evidence`)
- Validates each pack against the canonical VEIP schema
- Stores packs in a local in-memory store (stub)
- Serves retrieval endpoints (`GET /v1/evidence/{evidence_id}`)
- Provides unit tests validating schema and API behavior

---

## What This Repository Is Not

The VEIP Registry is **not**:

- The VEIP Verifier Core (conformance engine)
- A certification authority
- A production WORM datastore
- A supervisory endorsement system
- A centralized “global registry”

This is a reference surface, not a governance authority.

---

## Relationship to veip-spec

The canonical Evidence Pack schema originates in:

