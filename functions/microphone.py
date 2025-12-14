import sounddevice as sd
import os
from scipy.io.wavfile import write
from dotenv import load_dotenv
load_dotenv()  

file_path = os.getenv("FILE_PATH")
extend = "\\"
microphone_time = 10  # Set the duration for microphone recording
audio_information = "audio.wav"

def microphone():
    fs = 44100
    seconds = microphone_time  # Use the global microphone_time variable
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until the recording is finished
    write(file_path + extend + audio_information, fs, myrecording)