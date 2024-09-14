from abc import ABC, abstractmethod
from typing import Tuple


class GeneratorAPI(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.api_key = None

    @abstractmethod
    def refresh_token(self) -> None:
        pass

    @abstractmethod
    def call_api(self, query: str) -> Tuple[str]:
        pass
