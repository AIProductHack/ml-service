import os
from typing import Tuple
import requests
import uuid

from .base import GeneratorAPI
from .prompt import prompt


class GigachatAPI(GeneratorAPI):
    def __init__(self) -> None:
        super().__init__()
        self.refresh_token()

    def refresh_token(self) -> None:
        authorization_data = os.getenv("GIGACHAT_AUTHORIZATION_DATA")
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        payload = 'scope=GIGACHAT_API_PERS'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': uuid.uuid4(),
            'Authorization': f'Basic {authorization_data}'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        self.api_key = response.json()['access_token']

    def call_api(self, prompt: Tuple, query: str) -> Tuple[str, str]:
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "GigaChat:latest",
            "messages": [
                {"role": "system", "content": prompt[0]},
                {"role": "user", "content": query}
            ],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=data, verify=False)
        return response.json()['choices'][0]['message']['content']
