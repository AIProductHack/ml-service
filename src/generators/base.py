from typing import Any
from abc import ABC, abstractmethod


class GeneratorModel(ABC):
    def __init__(self, api_key: str) -> None:
        super().__init__()
        self.api_key = api_key

    @abstractmethod
    def refresh_token(self) -> None:
        pass

    @abstractmethod
    def call_api(self) -> dict[str, Any]:
        pass
