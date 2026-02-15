# veip_registry/schema.py
from __future__ import annotations

import json
from importlib import resources
from typing import Any, Dict

from jsonschema import Draft202012Validator


_SCHEMA_REL_PATH = "schemas/veip-evidence-pack.schema.json"


def load_schema() -> Dict[str, Any]:
    """
    Load the canonical VEIP Evidence Pack JSON Schema from packaged data.

    This works both:
      - in a git checkout, and
      - after `pip install` (incl. editable installs),
    as long as the schema is included as package data.
    """
    try:
        schema_file = resources.files("veip_registry").joinpath(_SCHEMA_REL_PATH)
        with schema_file.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Missing packaged schema '{_SCHEMA_REL_PATH}'. "
            "Ensure the file exists at veip_registry/schemas/veip-evidence-pack.schema.json "
            "and that pyproject.toml includes it under [tool.setuptools.package-data]."
        ) from e


def validate_evidence_pack(evidence_pack: Dict[str, Any]) -> None:
    """
    Validate a VEIP Evidence Pack against the canonical schema.

    Raises jsonschema.ValidationError on schema violations.
    """
    schema = load_schema()
    Draft202012Validator(schema).validate(evidence_pack)
