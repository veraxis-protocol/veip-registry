from typing import Any, Dict


class InMemoryStore:
    def __init__(self) -> None:
        self._by_id: Dict[str, Dict[str, Any]] = {}

    def put(self, evidence_id: str, pack: Dict[str, Any]) -> None:
        if evidence_id in self._by_id:
            raise KeyError("exists")
        self._by_id[evidence_id] = pack

    def get(self, evidence_id: str) -> Dict[str, Any]:
        return self._by_id[evidence_id]
