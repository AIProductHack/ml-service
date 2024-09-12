from .base import GeneratorAPI
import requests
import json
import time
import jwt
import os
from .prompt import prompt


class YandexGTPAPI(GeneratorAPI):
    def __init__(self) -> None:
        super().__init__()
        self.refresh_token()

    def refresh_token(self) -> None:
        
        now = int(time.time())
        payload = {
            'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
            'iss': os.getenv("ygpt_service_account_id"),
            'iat': now,
            'exp': now + 360}

        # Формирование JWT
        encoded_token = jwt.encode(
            payload,
            os.getenv("ygpt_private_key"),
            algorithm='PS256',
            headers={'kid': os.getenv("ygpt_key_id")})

        url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
        x = requests.post(url, headers={'Content-Type': 'application/json'}, json={'jwt': encoded_token}).json()
        token = x['iamToken']
        self.api_key = x['iamToken']

    def call_api(self, query, promt=prompt) -> str:

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
            {
                "role": "system",
                "text": promt
            },
            {
                "role": "user",
                "text": query
            }
        ]
        response = requests.post(url, headers={'Authorization': 'Bearer ' + self.api_key}, json=data).json()
        return response['result']['alternatives'][0]['message']['text']