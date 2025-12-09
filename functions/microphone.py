import sounddevice as sd
from scipy.io.wavfile import write

file_path = "C:\\Users\\PC-Service\\OneDrive\\Desktop\\project\\files\\"
extend = "\\"
microphone_time = 10  # Set the duration for microphone recording
audio_information = "audio.wav"

def microphone():
    fs = 44100
    seconds = microphone_time  # Use the global microphone_time variable
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until the recording is finished
    write(file_path + extend + audio_information, fs, myrecording)