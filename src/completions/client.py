import os

from openai import OpenAI

class OllamaClient:
    def __init__(
        self,
        model: str | None = None,
        base_url: str | None = None,
    ) -> None:
        self.model = model or os.getenv("OLLAMA_MODEL")
        resolved_url = base_url or os.getenv("OLLAMA_BASE_URL")

        if not self.model:
            raise ValueError("Set OLLAMA_MODEL in your .env file.")

        if not resolved_url:
            raise ValueError("Set OLLAMA_BASE_URL in your .env file.")

        self.client = OpenAI(
            base_url=resolved_url,
            api_key="ollama",  # Placeholder required by the SDK.
        )

    def chat(
        self,
        prompt: str,
        system: str = "You are a super-duper, helpful, assistant.",
    ) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
        )

        return response.choices[0].message.content or ""