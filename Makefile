SHELL := /bin/bash
.PHONY: help check test ci run

help:
	@echo "Targets:"
	@echo "  make check  - basic structural + schema checks"
	@echo "  make test   - run unit tests"
	@echo "  make ci     - check + test"
	@echo "  make run    - start local registry API (stub)"

check:
	@set -euo pipefail; \
	req=(README.md pyproject.toml veip_registry/app.py veip_registry/schemas/veip-evidence-pack.schema.json); \
	for f in "${req[@]}"; do \
	  if [[ ! -f "$$f" ]]; then echo "Missing required file: $$f"; exit 1; fi; \
	done
	@python -c "import json,pathlib; p=pathlib.Path('veip_registry/schemas/veip-evidence-pack.schema.json'); json.loads(p.read_text(encoding='utf-8')); print('OK: schema JSON parses')"
	@echo "OK: checks passed"

test:
	@pytest -q

ci: check test

run:
	@uvicorn veip_registry.app:app --host 127.0.0.1 --port 8080
