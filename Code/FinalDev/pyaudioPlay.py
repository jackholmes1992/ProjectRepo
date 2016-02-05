"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys

CHUNK = 1024

"""if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)
"""
#wf = wave.open(sys.argv[1], 'rb')
wf = wave.open('first.wav', 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)
print("before")

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)
    #print(data)
    if data == b'': #End of file - may affect playback
        print("breaking")
        break

    
print("done")
stream.stop_stream()
stream.close()

p.terminate()

