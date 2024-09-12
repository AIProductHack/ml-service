import enum
from .base import GeneratorAPI
from .yandexgpt import YandexGTPAPI
from .gigachat import GigachatAPI
from .chatgpt import ChatGPTAPI


class GeneratorType(str, enum.Enum):
    CHATGPT = "chatgpt"
    GIGACHAT = "gigachat"
    YANDEXGPT = "yandexgpt"


class GeneratorFactory:
    @classmethod
    def get_generator(cls, generator_type: str) -> type[GeneratorAPI]:
        match generator_type:
            case GeneratorType.CHATGPT.value:
                return ChatGPTAPI()
            case GeneratorType.YANDEXGPT.value:
                return YandexGTPAPI()
            case GeneratorType.GIGACHAT.value:
                return GigachatAPI()
