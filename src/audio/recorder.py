import pyaudio
import wave
import os

class AudioRecorder:
    def __init__(self, save_folder, filename="myaudio.wav", rate=44100, chunk=512, channels=1, format=pyaudio.paInt16):
        self.save_folder = save_folder
        self.filename = filename
        self.rate = rate
        self.chunk = chunk
        self.channels = channels
        self.format = format
        self.frames = []
        self.wave_output_path = os.path.join(self.save_folder, self.filename)
        os.makedirs(self.save_folder, exist_ok=True)
        self.p = pyaudio.PyAudio()
        self.stream = None

    def record(self):
        try:
            self.stream = self.p.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer=self.chunk)

            print("* Recording started... Press Ctrl+C to stop")
            self.frames = []

            while True:
                try:
                    data = self.stream.read(self.chunk, exception_on_overflow=False)
                    self.frames.append(data)
                except IOError:
                    print("Warning: Buffer overflow - continuing...")
                    continue

        except KeyboardInterrupt:
            print("\n* Recording stopped by user")
        except Exception as e:
            print(f"✗ Recording failed: {e}")

    def save(self):
        if not self.frames:
            print("✗ No audio data recorded")
            return

        try:
            with wave.open(self.wave_output_path, 'wb') as wf:
                wf.setnchannels(self.channels)
                wf.setsampwidth(self.p.get_sample_size(self.format))
                wf.setframerate(self.rate)
                wf.writeframes(b''.join(self.frames))

            duration = len(self.frames) * self.chunk / self.rate
            file_size = os.path.getsize(self.wave_output_path) / 1024  # KB

            print(f"✓ Saved to {self.wave_output_path}")
            print(f"  Duration: {duration:.1f} seconds")
            print(f"  Size: {file_size:.1f} KB")

        except Exception as e:
            print(f"✗ Saving failed: {e}")

    def cleanup(self):
        try:
            if self.stream and self.stream.is_active():
                self.stream.stop_stream()
            if self.stream:
                self.stream.close()
            self.p.terminate()
        except:
            pass

    def run(self):
        try:
            self.record()
        finally:
            self.save()
            self.cleanup()


if __name__ == "__main__":
    recorder = AudioRecorder(
        save_folder=r"C:/Users/ADMIN/OneDrive/Desktop/STS/local-speech-to-speech/data/samples/",
        filename="myaudio.wav"
    )
    recorder.run()
