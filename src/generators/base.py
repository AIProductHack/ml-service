import requests
from abc import ABC, abstractmethod

class GeneratorAPI(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def refresh_token(self) -> None:
        pass


    @abstractmethod
    def call_api(self) -> str:
        pass
