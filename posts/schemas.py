from typing import Dict, Optional
from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    author: str
    text: str
    keywords: str

class EditPostRequest(BaseModel):
    author: Optional[str] = None
    text: Optional[str] = None
    keywords: Optional[str] = None

class GenerationRequest(BaseModel):
    keywords: str


