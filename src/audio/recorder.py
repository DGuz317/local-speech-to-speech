import pyaudio
import wave
import os

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
SAVE_FOLDER = r"C:/Users/ADMIN/OneDrive/Desktop/STS/local-speech-to-speech/data/samples/"
os.makedirs(SAVE_FOLDER, exist_ok=True)
WAVE_OUTPUT_FILENAME = os.path.join(SAVE_FOLDER, "myaudio.wav")

p = pyaudio.PyAudio()
stream = None
wf = None

try:
    # Open audio stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* Recording started...")
    print(f"  Duration: {RECORD_SECONDS} seconds")
    frames = []

    # Record audio
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        try:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
        except IOError as e:
            print(f"Warning: Buffer overflow - continuing...")
            continue

    print("* Recording complete")
    
    # Save the recorded audio file
    if frames:
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        
        # Calculate file info
        duration = len(frames) * CHUNK / RATE
        file_size = os.path.getsize(WAVE_OUTPUT_FILENAME) / 1024  # KB
        
        print(f"✓ Saved to {WAVE_OUTPUT_FILENAME}")
        print(f"  Duration: {duration:.1f} seconds")
        print(f"  Size: {file_size:.1f} KB")
    else:
        print("✗ No audio data recorded")

except IOError as e:
    print(f"✗ Recording failed: {e}")
    print("Check that your microphone is connected and not in use.")
except KeyboardInterrupt:
    print("\n✗ Recording interrupted by user")
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    
finally:
    # Cleanup stream
    if stream is not None:
        try:
            if stream.is_active():
                stream.stop_stream()
            stream.close()
        except:
            pass
    
    # Cleanup PyAudio
    if p is not None:
        try:
            p.terminate()
        except:
            pass
    
    # Cleanup wave file
    if wf is not None:
        try:
            wf.close()
        except:
            pass