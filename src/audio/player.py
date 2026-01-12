import pyttsx3

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
        print(f"🎤 Speaking: {text[:50]}...")  # preview first 50 chars
        self.engine.say(text)
        self.engine.runAndWait()

    def speak_from_file(self, filepath: str):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            self.speak(text)
        except FileNotFoundError:
            print(f"✗ File not found: {filepath}")
        except Exception as e:
            print(f"✗ Error reading file: {e}")


if __name__ == "__main__":
    player = TextToSpeechPlayer(rate=160, volume=1.0, voice="female")

    # Option 1: Speak user input
    # text_input = input("Enter text to speak: ")
    # player.speak(text_input)

    # Option 2: Speak from text.txt
    player.speak_from_file(r"C:\Users\ADMIN\OneDrive\Desktop\STS\local-speech-to-speech\data\samples\text.txt")
