# Threat Model (Stub)

Threats addressed here:
- Malformed evidence: rejected by strict schema validation.
- Overwrite attempts: evidence_id collision rejected (409).
- Accidental schema drift: canonical schema is vendored and checked by CI.

Not addressed in this stub (production concerns):
- Authn/authz, rate limiting, abuse prevention
- WORM storage guarantees
- Cryptographic sealing / signatures
- Time-source integrity
- Replication and availability
