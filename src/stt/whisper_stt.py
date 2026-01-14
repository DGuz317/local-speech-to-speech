import whisper

def transcribe_audio(audio_path: str) -> str:
    model = whisper.load_model("base")  # You can try "small", "medium", or "large" later
    result = model.transcribe(audio_path)
    return result["text"].strip()
