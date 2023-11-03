import pyaudio
import wave
import numpy as np
import time
import pyautogui

# Set the parameters for audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Size of each audio chunk (number of frames per buffer)
RECORD_SECONDS = 0.5  # Duration of each recording in seconds


# Initialize PyAudio
audio = pyaudio.PyAudio()

time.sleep(7)
try:
    while True:
        
        # Open the audio stream
        stream = audio.open(format=FORMAT, 
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            input_device_index=1,
                            frames_per_buffer=CHUNK)
        
        #print("Recording...")
        frames = []

        # Record audio for the specified duration
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        #print("Finished recording.")

        # Close the audio stream
        stream.stop_stream()
        stream.close()

        # Calculate RMS amplitude
        audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
        rms_amplitude = np.sqrt(np.mean(audio_data ** 2))

        
        if rms_amplitude > 25:
            print(f"RMS Amplitude: {rms_amplitude}")
            print("Fish Detected")
            pyautogui.mouseDown(); 
            time.sleep(0.01)
            pyautogui.mouseUp()
            time.sleep(1)
            pyautogui.mouseDown(); 
            time.sleep(0.01)
            pyautogui.mouseUp()
            time.sleep(1)


finally:


    audio.terminate()
    