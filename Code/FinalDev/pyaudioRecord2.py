import pyaudio
import wave
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
p = pyaudio.PyAudio()

def record(file_name):

  stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = CHUNK)

  frames = []
  print ("starting recording " + file_name + ".")
  for i in range(0, int(RATE / CHUNK * 2)):
    data = stream.read(CHUNK)
    frames.append(data)
  print ("finished recording")

  stream.stop_stream()
  stream.close()

  wf = wave.open(file_name, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(p.get_sample_size(FORMAT))
  wf.setframerate(RATE)
  wf.writeframes(b''.join(frames))
  wf.close()

record('first.wav')
# try again
#record('second.wav')
os.system("python pyaudioPlay.py first.wav")
p.terminate()

