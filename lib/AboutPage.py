from tkinter import *
import tkinter.font as font


import os
def do():

    root = Tk()
    lblFont = font.Font(family='Helvetica', size=20)
    #root.geometry("250x150+300+300")
    root.title("Roses are red, violets are blue, No matter what, I will always love you")
    here = os.path.abspath(os.path.join(os.path.dirname( __file__ )))
    filename = os.path.join(here,'rose.gif')
    print(filename)
    img = PhotoImage(file= filename)
    bmpFileName = os.path.join(here, 'circle.bmp')
    #root.call('wm', 'iconphoto', root._w, img)
    lbl = Label(root, text= "Made by Scriptslay3r. \nI started this project becuase me and my infant daughter got seperated.\nI missed her and wanted to feel connected to her.", font = lblFont)
    lbl.pack()
    exitBtn = Button(root, text = "Exit")
    exitBtn.config(bitmap = 'info')
    exitBtn.pack()
    root.mainloop()


