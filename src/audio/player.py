from pydub import AudioSegment
from pydub.playback import play
import pyttsx3
import os

class TextToSpeechPlayer:
    def __init__(self, rate=150, volume=1.0, voice=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

        if voice:
            voices = self.engine.getProperty('voices')
            for v in voices:
                if voice.lower() in v.name.lower():
                    self.engine.setProperty('voice', v.id)
                    break

    def speak(self, text: str):
        if not text.strip():
            print("✗ No text provided")
            return
        print(f"🎤 Speaking: {text[:50]}...")
        self.engine.say(text)
        self.engine.runAndWait()

    def speak_from_text_file(self, filepath: str):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            self.speak(text)
        except Exception as e:
            print(f"✗ Error reading text file: {e}")

    def play_audio_file(self, filepath: str):
        if not os.path.exists(filepath):
            print(f"✗ Audio file not found: {filepath}")
            return
        try:
            audio = AudioSegment.from_file(filepath)
            print(f"🔊 Playing audio file: {filepath}")
            play(audio)
        except Exception as e:
            print(f"✗ Error playing audio file: {e}")
