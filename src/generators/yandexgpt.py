from .base import GeneratorAPI


class YandexGTPAPI(GeneratorAPI):
    def __init__(self) -> None:
        super().__init__()

    def refresh_token(self) -> None:
        pass

    def call_api(self) -> str:
        pass
