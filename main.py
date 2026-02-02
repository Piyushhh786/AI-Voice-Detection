from tamper_pipeline.manual_pipeline import base64_to_wav,extract_whisper_features
import base64
import whisper
import torch
import numpy as np
import torch
model = whisper.load_model("base")




def predict_voice(base64_audio, svm_model):
    audio = base64_to_wav(base64_audio)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    with torch.no_grad():
        emb = model.encoder(mel.unsqueeze(0))

    # Fixed-length vector
    X = emb.mean(dim=1).cpu().numpy().flatten()
    X = np.array(X)
    X = X.reshape(1, -1)

    label = svm_model.predict(X)[0]
    confidence = svm_model.predict_proba(X)[0]

    return {
        "prediction": "AI" if label == 1 else "Human",
        "confidence": {
            "human": float(confidence[0]),
            "ai": float(confidence[1])
        }
    }

def audio_to_base64(audio_path):
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
    return base64.b64encode(audio_bytes).decode("utf-8")

# Example
b64_audio = audio_to_base64("test/real/hindi/common_voice_te_43371454.mp3")
print(b64_audio[:100])  # preview

import joblib

svm_model = joblib.load("whisper_svm_ai_vs_human.pkl")

x = predict_voice(b64_audio,svm_model)
print(x)

