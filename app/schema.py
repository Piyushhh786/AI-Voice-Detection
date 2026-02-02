from pydantic import BaseModel
from typing import Literal

class VoiceRequest(BaseModel):
    language: Literal["Tamil", "English", "Hindi", "Malayalam", "Telugu"]
    audioFormat: Literal["mp3"]
    audioBase64: str

class VoiceResponse(BaseModel):
    status: str
    language: str
    classification: str
    confidenceScore: float
    explanation: str
