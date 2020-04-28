import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import datetime
import subprocess
import re
import os
import pickle



class myRose(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.iconbitmap("rose.ico")
        self.title("Roses are red, violets are blue, No matter what, I will always love you")
        self.geometry("800x480")
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
   
    def __init__(self,master):
        """   this is the "main frame from tkinter """
        tk.Frame.__init__(self,master)
        """this is the label on the front page"""
        tk.Label(self, text="What Do You Want To Do Today? :)").pack(side="top", fill="x", pady=10)
        """Where I start defining my buttons"""
        babyName = "babyName.pckl" 
        
        if not os.path.exists(babyName):
         
            name = simpledialog.askstring("Input", "What is your baby's name?")
            f = open('babyName.pckl', 'wb')
            pickle.dump(name, f)
            tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)

        else:
            b = open(babyName, 'rb')
            baby = pickle.load(b)
            tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + baby)
            
        storyBtn = tk.Button(self, text="Story Time!",
                    command=lambda: master.switch_frame(StoryPage))
        gameBtn = tk.Button(self, text="Games! :)",
                    command=lambda: master.switch_frame(GamePage))
        settingsBtn = tk.Button(self, text = "Mommy and Daddy Settings",
                    command=lambda: master.switch_frame(SettingPage))
        
        """running a command to get public IP address, and assigning it a variable"""

        
        
        """this is where I put the buttons in order"""
        storyBtn.pack()
        gameBtn.pack()
        settingsBtn.pack()
        

if __name__ == "__main__":
    #checkName()
    app = myRose()
    app.mainloop()
    