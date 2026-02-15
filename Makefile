SHELL := /bin/bash
.PHONY: help check test ci run

help:
	@echo "Targets:"
	@echo "  make check  - basic sanity checks"
	@echo "  make test   - run unit tests"
	@echo "  make ci     - check + test"
	@echo "  make run    - start local registry API (stub)"

check:
	@set -euo pipefail; \
	req=(README.md LICENSE LICENSE.md schemas/veip-evidence-pack.schema.json veip_registry/app.py); \
	for f in "$${req[@]}"; do \
	  if [[ ! -f "$$f" ]]; then echo "Missing required file: $$f"; exit 1; fi; \
	done; \
	python - <<'PY' \
import json, pathlib, sys \
p = pathlib.Path("schemas/veip-evidence-pack.schema.json") \
json.loads(p.read_text(encoding="utf-8")) \
print("OK: schema JSON parses") \
PY
	@echo "OK: checks passed"

test:
	@pytest -q

ci: check test

run:
	@uvicorn veip_registry.app:app --host 127.0.0.1 --port 8080
