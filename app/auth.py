import os
from fastapi import Header, HTTPException

API_KEY = os.getenv("API_SECRET_KEY")
# API_KEY = "TOP_SECRET"

if not API_KEY:
    raise RuntimeError("API_SECRET_KEY is not set")

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail={
                "status": "error",
                "message": "Invalid API key or malformed request"
            }
        )
