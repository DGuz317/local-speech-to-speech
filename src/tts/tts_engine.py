from gtts import gTTS

def synthesize_speech(text: str, output_path: str = "data/samples/tts_output.mp3"):
    if not text.strip():
        print("✗ No text to synthesize")
        return
    tts = gTTS(text=text, lang="en")
    tts.save(output_path)
    print(f"✓ TTS saved to {output_path}")
