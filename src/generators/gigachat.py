import os
from .base import GeneratorAPI


class GigachatAPI(GeneratorAPI):

    def refresh_token(self) -> None:
        rid = os.getenv("GIGACHAT_RID")
        secret = os.getenv("GIGACHAT_SECRET")
        url = "Y2JjZjcwMzMtZWFlYy00NWMxLTg0MTItMTFhMzliNjUwMTcwOmJmMWRmMTU0LTEzOWYtNGY5MC1hYjQ3LTIyMzY3NWFiMTQ3Zg=="

        payload = 'scope=GIGACHAT_API_PERS'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': rid,
            'Authorization': f'Basic {secret}'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        self.api_key = response.json()['access_token']

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

