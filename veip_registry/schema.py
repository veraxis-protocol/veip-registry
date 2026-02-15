import json
import pathlib
from typing import Any, Dict

from jsonschema import Draft202012Validator

_SCHEMA_PATH = pathlib.Path(__file__).resolve().parents[1] / "schemas" / "veip-evidence-pack.schema.json"


def load_schema() -> Dict[str, Any]:
    return json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))


def validate_evidence_pack(pack: Dict[str, Any]) -> None:
    schema = load_schema()
    Draft202012Validator(schema).validate(pack)
