from typing import Protocol, runtime_checkable


@runtime_checkable
class IReport(Protocol):
    def get_json_data(self, base_data: str) -> str: ...
