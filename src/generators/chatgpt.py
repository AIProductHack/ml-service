import json
import os
from typing import Tuple
from openai import OpenAI
from .prompt.prompt_chatgpt import prompt

from .base import GeneratorAPI


class ChatGPTAPI(GeneratorAPI):
    def __init__(self) -> None:
        super().__init__()
        self.api_key = os.environ['CHATGPT_API_KEY']
        self.client = OpenAI(
            api_key=f"{self.api_key}",
            base_url="https://api.proxyapi.ru/openai/v1",
        )

    def refresh_token(self) -> None:
        raise Exception("Don't call refresh_token() for ChatGPT")

    def call_api(self, query: str) -> Tuple[str, str]:
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query}
            ],
            temperature=0.5,
            response_format={"type": "json_object"}
        )
        result = json.loads(response.choices[0].message.content)
        return str(result['components']), result['css']
