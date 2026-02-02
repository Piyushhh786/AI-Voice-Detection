from pydantic import BaseModel
from typing import Literal

class VoiceRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str

class VoiceResponse(BaseModel):
    status: str
    language: str
    classification: str
    confidenceScore: float
    explanation: str
