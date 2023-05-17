import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 20  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
print('Starting recording now...')
sd.wait()  # Wait until recording is finished
print('Ending recording now...')
write('output_jin.wav', fs, myrecording)  # Save as WAV file 
