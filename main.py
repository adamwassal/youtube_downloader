from pytube import YouTube
from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("Youtube downloader")


entry = Entry(root, width=50)
entry.pack()

button_show = Button(root, text="Show Resolutions", command=lambda: show_resolutions_func(url = entry.get()))
button_show.pack()

resolutions = []
n = tk.StringVar() 
sel = ttk.Combobox(root,textvariable = n)
sel.pack()

button_down = Button(root, text="Download", command=lambda: download_youtube_video(url = entry.get(), download_path = ''))
button_down.pack()

label_down = Label(root, text="")
label_down.pack()


def show_resolutions_func(url = entry.get()):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    sel['values'] = ''
    resolutions = [stream.resolution for stream in streams]
    sel['values'] = resolutions
    sel.set(resolutions[0])

def download_youtube_video(url = entry.get(), download_path = ''):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        stream = yt.streams.get_by_resolution(sel.get())
        
        # Download the video
       
        label_down.config(text=f"Downloading: {yt.title}")
        stream.download(download_path)
        label_down.config(text="Done")
    except Exception as e:
        print(f"An error occurred: {e}")

root.mainloop()