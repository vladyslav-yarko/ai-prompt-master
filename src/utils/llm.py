from typing import Optional

from g4f.client import AsyncClient
from g4f.Provider import Yqcloud

from src.config import settings


class LLM:
    def __init__(
        self, 
        model: Optional[None] = None,
        temperature: float = 0.5):
        # self.client = AsyncClient(
        #     # provider=Chatai
        # )
        self.client = AsyncClient(
            provider=Yqcloud
        )
        self.model = model if model is not None else settings.MODEL
        self.temperature = temperature
        
    async def ask(self, messages: list[dict]):
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.5
        )
        clean_response = response.choices[0].message.content
        return clean_response
