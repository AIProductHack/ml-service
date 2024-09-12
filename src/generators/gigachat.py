import os
from typing import Tuple
import requests
import uuid

from .base import GeneratorAPI
from .prompt.gigachat_prompt import prompt


class GigachatAPI(GeneratorAPI):
    def __init__(self) -> None:
        super().__init__()
        self.refresh_token()

    def refresh_token(self) -> None:
        authorization_data = os.getenv("GIGACHAT_SECRET")
        rid = os.getenv("GIGACHAT_RID")
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

        payload = 'scope=GIGACHAT_API_PERS'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': rid,
            'Authorization': f'Basic {authorization_data}'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        self.api_key = response.json()['access_token']

    def call_api(self, query: str, prompt: str = prompt, ) -> str:
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "GigaChat:latest",
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": query}
            ],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=data, verify=False)
        return response.json()['choices'][0]['message']['content']
