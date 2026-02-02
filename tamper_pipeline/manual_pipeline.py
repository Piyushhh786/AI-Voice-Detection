import base64
import soundfile as sf
import io
import numpy as np
import librosa
import tempfile
import os

def base64_to_wav(base64_audio):
    audio_bytes = base64.b64decode(base64_audio)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        temp_path = f.name

    # Whisper handles mp3 / wav / m4a automatically
    audio = whisper.load_audio(temp_path)

    os.remove(temp_path)
    return audio

#  -------------------------------------------------------------------------------------
# vectorization 
import whisper
import torch

whisper_model = whisper.load_model("base")

def extract_whisper_features(audio):
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(whisper_model.device)

    with torch.no_grad():
        embedding = whisper_model.encoder(mel.unsqueeze(0))

    # Convert to 1D vector
    features = embedding.mean(dim=1).squeeze().cpu().numpy()
    return features

