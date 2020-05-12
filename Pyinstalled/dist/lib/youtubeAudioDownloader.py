from __future__ import unicode_literals
import youtube_dl
import tkinter.font as font
from tkinter import simpledialog



def download():
    
    

    def submit():
        #savedName = simpledialog.askstring("Input", "What would you like to name this song?")
        c = box.get()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([c])
            
    try:
        # Python2
        import Tkinter as tk
    except ImportError:
        # Python3
        import tkinter as tk

    root = tk.Tk()
    root.title("Music Download")
    # read the clipboard
    try:
        c = root.clipboard_get()
    except (RuntimeError, TypeError, NameError):
        print("Error")

    headerFont = font.Font(family='Helvetica', size=20)
    header = tk.Label(root, text = "Look up the song on Youtube and copy the URL \nfrom the address bar in your browser. \nThen paste it in the box", font = headerFont)
    box = tk.Entry(root, width = 40)
    box.insert(0, c)
    submitBtn = tk.Button(root, text = "Download Audio", command = submit)
    exitBtn = tk.Button(root, text = "Exit", command = lambda: root.destroy())
    header.pack()
    box.pack()
    submitBtn.pack()
    exitBtn.pack()


    