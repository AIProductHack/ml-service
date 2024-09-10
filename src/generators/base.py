import requests
from abc import ABC, abstractmethod


class GeneratorAPI(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def refresh_token(self, rid='85edd55c-2805-441a-a7f1-839485b58c58', secret='') -> None:
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

        payload = 'scope=GIGACHAT_API_PERS'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': rid,
            'Authorization': f'Basic {secret}'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        self.api_key = response.json()['access_token']

    @abstractmethod
    def call_api(self, promt, quare) -> str:

        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        headers = {
            "Content-Type": "application/json",

            "Authorization": f"Bearer {self.api_key}"}

        data = {
            "model": "GigaChat:latest",
            "messages": [
                {"role": "system", "content": promt},
                {"role": "user", "content": quare}
            ],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=data, verify=False)
        return response.json()['choices'][0]['message']['content']

