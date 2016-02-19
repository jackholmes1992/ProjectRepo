from tkinter import *
from tkinter import ttk
import os
import threading
import wave
import pyaudio
import sys

# Thread fuction for play
def play_audio():
    chunk = 1024
    wf = wave.open('wav.wav', 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True)

    data = wf.readframes(chunk)

    print("playing")
    while data != '' and is_playing: #to stop playing
        stream.write(data)
        data = wf.readframes(chunk)
        #is_playing = False
        if data == b'': #End of file - may affect playback
            print("breaking")
            break

    print("finished playing")
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("closing play thread")

# Thread fuction for play
def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    p = pyaudio.PyAudio()
    
    stream = p.open(format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        input = True,
        frames_per_buffer = CHUNK)

    frames = []
    print ("starting recording...")
    for i in range(0, int(RATE / CHUNK * 2)):
        if is_recording: #to stop recording
            data = stream.read(CHUNK)
            frames.append(data)
    print ("finished recording")

    stream.stop_stream()
    stream.close()

    wf = wave.open('wav.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    p.terminate()

def playButton():
    try:
        global is_playing
        global my_thread

        #if not is_playing:
        is_playing = True
        my_thread = threading.Thread(target=play_audio)
        my_thread.start()
    except ValueError:
        pass

def stopPlayButton():
    try:
        global is_playing

        if is_playing:
            is_playing = False
            my_thread.join()           
    except ValueError:
        pass

def recordButton():
    try:
        global is_recording
        global record_thread

        if not is_recording:
            is_recording = True
            record_thread = threading.Thread(target=record_audio)
            record_thread.start()
    except ValueError:
        pass

def stopRecordButton():
    try:
        global is_recording

        if is_recording:
            is_recording = False
            record_thread.join()           
    except ValueError:
        pass


#### MAIN PROGRAM ####

is_playing = False
is_recording = False
my_thread = None
    
root = Tk()
root.title("Collaborative Audio System")

#root.geometry("400x300")
# Setup Tk mainframe
mainframe = ttk.Frame(root, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


# Treeview for showing takes
tree = ttk.Treeview(mainframe)
tree["columns"]=("one","two")
tree['show'] = 'headings' #hides first column
tree.column("one", width=100 )
tree.column("two", width=100)
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("" , 0,    text="Line 1", values=("1A","1b"))

id2 = tree.insert("", 1, "dir2", text="Dir 2")
tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))

# Setup buttons
#ttk.Treeview(mainframe).grid(column=0, row=0, sticky=E)
tree.grid(column=3, row=0, sticky=E)
ttk.Button(mainframe, text="Play", command=playButton).grid(column=3, row=2, sticky=E)
ttk.Button(mainframe, text="Stop Playing", command=stopPlayButton).grid(column=3, row=3, sticky=E)
ttk.Button(mainframe, text="Record", command=recordButton).grid(column=0, row=2, sticky=W)
ttk.Button(mainframe, text="Stop Recording", command=stopRecordButton).grid(column=0, row=3, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#root.bind('<Return>', calculate)
root.mainloop()
