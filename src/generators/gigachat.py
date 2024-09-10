import os
from .base import GeneratorAPI


class GigachatAPI(GeneratorAPI):

    def refresh_token(self) -> None:
        rid = os.getenv("GIGACHAT_RID")
        secret = os.getenv("GIGACHAT_SECRET")

    def call_api(self) -> str:
        pass
