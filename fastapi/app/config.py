from pydantic_settings import BaseSettings
from typing import List, Dict


class Settings(BaseSettings):
    app_name: str = "Word Counter"
    app_description: str = """
Simple API to count the number of words in a text."""
    tags_metadata: List[Dict] = [
        {"name": "WordCounter", "description": "Count number of words in a text."}
    ]


settings = Settings()
