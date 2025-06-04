from abc import ABC, abstractmethod


class IReport(ABC):
    @abstractmethod
    def get_json_data(self) -> str: ...
