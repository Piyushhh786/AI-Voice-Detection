from fastapi import FastAPI, Depends, HTTPException
from .schema import VoiceRequest, VoiceResponse
from .auth import verify_api_key
from .inference import predict_voice

app = FastAPI(title="AI-Generated Voice Detection API")

@app.post("/api/voice-detection", response_model=VoiceResponse)
def voice_detection(
    req: VoiceRequest,
    _: str = Depends(verify_api_key)
):
    try:
        label, confidence, explanation = predict_voice(req.audioBase64)

        return {
            "status": "success",
            "language": req.language,
            "classification": label,
            "confidenceScore": round(confidence, 2),
            "explanation": explanation
        }

    except Exception as e:
        # Catch EVERYTHING to avoid API crash during evaluation
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "message": "Audio processing failed or malformed request"
            }
        )