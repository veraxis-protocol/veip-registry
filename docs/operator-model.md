# Multi-Operator Registry Model (Stub)

Goal: avoid a single global registry bottleneck by enabling many compatible operators.

Properties:
1. Canonical artifact: Evidence Packs are portable because they validate against the canonical schema.
2. Operator replaceability: clients can switch registry operators without reformatting evidence.
3. Non-exclusive role: registry operation is not identical to certification; verifier core remains separate.
4. Concentration risk reduction: interoperability + public contract prevents lock-in.
5. Integrity preservation: schema validation is mandatory for intake; replay/verifier layers can be added upstream/downstream.

This stub demonstrates the minimal surface area required for interoperability.
