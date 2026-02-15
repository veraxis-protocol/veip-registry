import json
import pathlib

from veip_registry.schema import validate_evidence_pack

FIXTURE = pathlib.Path(__file__).resolve().parents[0] / "fixture_pack.json"


def test_schema_fixture_validates():
    pack = json.loads(FIXTURE.read_text(encoding="utf-8"))
    validate_evidence_pack(pack)
