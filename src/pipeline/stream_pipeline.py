from src.audio.recorder import AudioRecorder
from src.stt.whisper_stt import transcribe_audio
from src.tts.tts_engine import synthesize_speech
from src.audio.player import TextToSpeechPlayer

def run_pipeline():
    recorder = AudioRecorder(save_folder="data/samples", filename="input.wav")
    recorder.run()

    text = transcribe_audio("data/samples/input.wav")
    print(f"📝 Transcribed: {text}")

    output_path = synthesize_speech(text, output_path="data/samples/tts_output.mp3")

    if output_path:
        player = TextToSpeechPlayer()
        player.play_audio_file(output_path)   # 👈 use this for mp3 playback

if __name__ == "__main__":
    run_pipeline()
