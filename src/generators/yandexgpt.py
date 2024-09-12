import requests
import time
import jwt
import os
from typing import Tuple

from .base import GeneratorAPI
from .prompt import prompt


class YandexGTPAPI(GeneratorAPI):
    def __init__(self) -> None:
        super().__init__()
        self.refresh_token()

class YandexGPTAPI(GeneratorAPI):
    def refresh_token(self) -> None:
        
        now = int(time.time())
        payload = {
            'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
            'iss': os.getenv("YAGPT_SERVICE_ACCOUNT_ID"),
            'iat': now,
            'exp': now + 360}

        # Формирование JWT
        encoded_token = jwt.encode(
            payload,
            os.getenv("YAGPT_PRIVATE_KEY"),
            algorithm='PS256',
            headers={'kid': os.getenv("YAGPT_KEY_ID")})

        url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
        x = requests.post(url, headers={'Content-Type': 'application/json'}, json={'jwt': encoded_token}).json()
        self.api_key = x['iamToken']

    def call_api(self, prompt: Tuple, query: str) -> Tuple[str, str]:
        url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

        data = {}

        # Указываем тип модели
        # 'gpt://<идентификатор_каталога>/yandexgpt-lite'
        data['modelUri'] = 'gpt://b1g8rlmq0f0m4crnqr7p/yandexgpt-lite'

        # Настраиваем дополнительные параметры модели
        data['completionOptions'] = {'stream': False,
                                     'temperature': 0.5,
                                     'maxTokens': 100000}
        data['messages'] = [
            {"role": "system", "text": prompt[0]},
            {"role": "user", "text": query}
        ]
        response = requests.post(url, headers={'Authorization': 'Bearer ' + self.api_key}, json=data).json()
        return response['result']['alternatives'][0]['message']['text']


def parse_response(response: str) -> Tuple[str, str]:
    # ?????
    pass
