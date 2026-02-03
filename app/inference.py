import base64
import whisper
import torch
import numpy as np
import torch
import tempfile
import os
import joblib



device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("base").to(device)
svm_model = joblib.load("models/whisper_svm_ai_vs_human.pkl")

def base64_to_wav(base64_audio):
    audio_bytes = base64.b64decode(base64_audio)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        f.write(audio_bytes)
        temp_path = f.name

    # Whisper handles mp3 / wav / m4a automatically
    audio = whisper.load_audio(temp_path)

    os.remove(temp_path)
    return audio

def predict_voice(base64_audio, svm_model=svm_model):
    audio = base64_to_wav(base64_audio)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    # print("torch version: ",torch.__version__)
    with torch.no_grad():
        emb = model.encoder(mel.unsqueeze(0))

    # Fixed-length vector
    X = emb.mean(dim=1).cpu().numpy().flatten()
    X = np.array(X)
    X = X.reshape(1, -1)

    label = svm_model.predict(X)[0]
    confidence = float(svm_model.predict_proba(X)[0][label])
    label = "AI_GENERATED" if label == 1 else "HUMAN"
    explanation = (
        "Unnatural pitch consistency and robotic speech patterns detected"
        if label == "AI_GENERATED"
        else "Natural pitch variations and human-like speech characteristics detected"
    )

    return label,confidence,explanation

def audio_to_base64(audio_path):
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
    return base64.b64encode(audio_bytes).decode("utf-8")

# # Example
# b64_audio = audio_to_base64("../test/ai/hindi/fake_by_tts.mp3")
# print(b64_audio[:100])  # preview



# x = predict_voice(b64_audio,svm_model)
# print(x)

