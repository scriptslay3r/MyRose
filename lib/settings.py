from tkinter import *
import pickle
import emoji
import tkinter.font as font
######## Home page for Settings ########
root = Tk()
with open('babyName.pckl', 'rb') as b:
    baby = pickle.load(b)
headerFont = font.Font(family='Helvetica', size=20)

headerLbl = Label(root, text=emoji.emojize('Settings for mom and dad! \U00002699	'), font=headerFont).pack()
musicBtn = Button(root, text="Download Music For " + baby, command=lambda: youtubeAudioDownloader.download())
homeBtn = Button(root, text = "Go Home", command =lambda: master.switch_frame(StartPage))
musicBtn.pack()
homeBtn.pack()
root.mainloop()
