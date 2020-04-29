import tkinter as tk
from tkinter import simpledialog
import tkinter.font as font
from tkinter import messagebox
import datetime
import subprocess
import re
import os
import pickle
import emoji
from PIL import Image, ImageTk


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
        self._frame.grid()

class StartPage(tk.Frame):
   
    def __init__(self,master):
        headerFont = font.Font(family='Helvetica', size=20)
        """   this is the "main frame from tkinter """
        tk.Frame.__init__(self,master)
        """this is the label on the front page"""
        tk.Label(self, text="What Do You Want To Do Today? :)", font = headerFont).grid(row = 1, rowspan = 2, column= 4, columnspan= 2)

        """ This is for determining New Users, so allow the program to be more personalized"""

        babyName = "babyName.pckl" 
        
        """ If you are a new user, enter the baby's name"""
        if not os.path.exists(babyName):
         
            name = simpledialog.askstring("Input", "What is your baby's name?")
            f = open('babyName.pckl', 'wb')
            pickle.dump(name, f)
            tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)
         #If you are not a new user, welcome back
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
        
        
        
        
        """this is where I put the buttons in order"""
        storyBtn.grid(row = 4, column = 2)
        gameBtn.grid(row = 4, column = 3)
        settingsBtn.grid(row = 4, column = 4)

###### Home page with the story interactions 

class StoryPage(tk.Frame):
   
    def __init__(self,master):
        headerFont = font.Font(family='Helvetica', size=20)
        """   this is the "main frame from tkinter """
        tk.Frame.__init__(self,master)
        """this is the label on the front page"""
        tk.Label(self, text=emoji.emojize('Story Time!\U0001f600 '), font = headerFont).grid(row = 0, column= 2, columnspan= 2)
        storyBox = tk.Text(self, height = 4, width = 55)
        storyText = "Ahhhh, well hello there!! \nHow are you doing today? \nWell, what do you want to be today?"
        storyBox.insert(tk.END, storyText)
        s = tk.Scrollbar(self, orient = 'vertical')
        
        
        s.config(command=storyBox.yview)



       
            
        boyBtn = tk.Button(self, text="I want to be an astronaut!",
                    command=lambda: master.switch_frame(astronautPage))
        girlBtn = tk.Button(self, text="I want to be a princess!",
                    command=lambda: master.switch_frame(princessPage))
        settingsBtn = tk.Button(self, text = "Mommy and Daddy Settings",
                    command=lambda: master.switch_frame(SettingPage))
        
        
        
        
        """this is where I put the buttons in order"""
        storyBox.grid(row = 2, column = 2)
        s.grid(row = 2, column = 2, sticky= 'e', ipady=50)
        boyBtn.grid(row = 4, column = 1)
        girlBtn.grid(row = 4, column = 2)
        settingsBtn.grid(row = 4, column = 4)

### One of the story interaction options 

class astronautPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self,master)
        headerLbl = tk.Label(self, text="Alright, junior astronaut \nLet's go explore space!")
        #searchBtn = tk.Button(self, text="Search")
        
        headerLbl.pack(pady='5')
        image = Image.open("astronaut.png")
        photo = ImageTk.PhotoImage(image)
        photoLabel = tk.Label(self, image=photo)
        photoLabel.image = photo
        photoLabel.pack(side='right')
        #searchBtn.pack(pady='5')
        tk.Button(self, text="Go Home",
                    command=lambda: master.switch_frame(StoryPage)).pack()

### One of the story interaction options
class princessPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self,master)
        headerLbl = tk.Label(self, text="Alright, little princess \nLet's go explore your kingdom!")
        #searchBtn = tk.Button(self, text="Search")
        
        headerLbl.pack(pady='5')
        image = Image.open("princess.png")
        photo = ImageTk.PhotoImage(image)
        photoLabel = tk.Label(self, image=photo)
        photoLabel.image = photo
        photoLabel.pack(side='right')
        #searchBtn.pack(pady='5')
        tk.Button(self, text="Go Home",
                    command=lambda: master.switch_frame(StoryPage)).pack()




        

if __name__ == "__main__":
    #checkName()
    app = myRose()
    app.mainloop()
    