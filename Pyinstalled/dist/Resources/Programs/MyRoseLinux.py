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
from playsound import playsound
from time import sleep

babyName = "babyName.pckl" 
babyGender = "babyGender.pckl"
class myRose(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #here = os.path.dirname(os.path.abspath(__file__))

        #icon = os.path.join(here, 'rose.ico')
        self.title("Roses are red, violets are blue, No matter what, I will always love you")
        img = tk.PhotoImage(file='rose.gif')
        self.tk.call('wm', 'iconphoto', self._w, img)
        #self.geometry("800x480")
        self._frame = None
            ##### Come back and add the ability for the program to detect the pickle files. if no files, open Setup, else open StartPage
        if not os.path.exists(babyGender):     
            self.switch_frame(setup)

        else:
            self.switch_frame(StartPage)
        

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

######## The Setup Page ########

class setup(tk.Frame):
   
    def __init__(self,master):
        headerFont = font.Font(family='Helvetica', size=20)
        subHeaderFont = font.Font(family='Helvetica', size=12)
        buttonFont = font.Font(family='Helvetica', size = 10, weight = 'bold')
        """   this is the "main frame from tkinter """
        tk.Frame.__init__(self,master)

        """this is the label on the front page"""
        header = tk.Label(self, text="Welcome to the setup page for My Rose!! :)", font = headerFont)
        subHeader = tk.Label(self, text="If you wouldn't mind filling out some information below, \nit will allow for a more personalized experience :)", font = subHeaderFont)
       # """ This is for determining New Users, so allow the program to be more personalized"""
        
        babyName = "babyName.pckl" 
        babyGender = "babyGender.pckl"
        var = tk.IntVar()
        
        def submitButtons():
            babyName = "babyName.pckl" 
            babyGender = "babyGender.pckl"
            selection = var.get()
            print(selection)
            ##### Boy Selection
            if selection == 1:
                if not os.path.exists(babyGender):
                    fGender = open('babyGender.pckl', 'wb')
                    pickle.dump("Boy", fGender)
                    name = simpledialog.askstring("Input", "Awwe, well congrats on your little boy! \nWhat is your son's name?")
                    fName = open('babyName.pckl', 'wb')
                    pickle.dump(name, fName)
                    tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)
                    self.switch_frame(StartPage)
                else:
                    b = open(babyName, 'rb')
                    baby = pickle.load(b)
                    #### Come Back And Add An Option to prompt if the user wants to continue anyway, deleting the old record
                    tk.messagebox.showwarning(title="Watch out now!!", message="It looks like you have already set up little baby " + baby)
                    MsgBox = tk.messagebox.askquestion ('Continue?','You can continue with the setup, it will delete ' + baby ,icon = 'warning')
                    if MsgBox == 'yes':
                        fGender = open('babyGender.pckl', 'wb')
                        pickle.dump("Boy", fGender)
                        name = simpledialog.askstring("Input", "Awwe, well congrats on your little boy! \nWhat is your son's name?")
                        fName = open('babyName.pckl', 'wb')
                        pickle.dump(name, fName)
                        tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)
                        self.switch_frame(StartPage)

                

            ##### Girl Selection
            elif selection == 2:
                if not os.path.exists(babyGender):
                    fGender = open('babyGender.pckl', 'wb')
                    pickle.dump("Girl", fGender)
                    name = simpledialog.askstring("Input", "Awwe, well congrats on your little girl! \nWhat is your daughter's name?")
                    fName = open('babyName.pckl', 'wb')
                    pickle.dump(name, fName)
                    tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)
                    master.switch_frame(StartPage)
                else:
                    b = open(babyName, 'rb')
                    baby = pickle.load(b)
                    #### Come Back And Add An Option to prompt if the user wants to continue anyway, deleting the old record
                    tk.messagebox.showwarning(title="Watch out now!!", message="It looks like you have already set up little baby " + baby)
                    MsgBox = tk.messagebox.askquestion ('Continue?','You can continue with the setup, it will delete ' + baby ,icon = 'warning')
                    if MsgBox == 'yes':
                        fGender = open('babyGender.pckl', 'wb')
                        pickle.dump("Girl", fGender)
                        name = simpledialog.askstring("Input", "Awwe, well congrats on your little girl! \nWhat is your daughter's name?")
                        fName = open('babyName.pckl', 'wb')
                        pickle.dump(name, fName)
                        tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)
                        master.switch_frame(StartPage)
            elif selection == 0:
                tk.messagebox.showwarning(title="Uh Oh! :/", message="Please make sure you selection something and try again :)")
            
            else:
                tk.messagebox.showwarning(title="Uh Oh! :/", message="Something went wrong :((")



        boyBtn = tk.Radiobutton(self, text = "A Baby Boy", variable = var, value = 1, indicatoron = 0, bg = "RoyalBlue", font = buttonFont)
        girlBtn = tk.Radiobutton(self, text = "A Baby Girl", variable = var, value = 2, indicatoron = 0, bg = "Pink", font = buttonFont )
        submitBtn = tk.Button(self, text = "Test Value", command = submitButtons)
        """ Set up the personalization by adding baby's name"""


    
        
        
        """this is where I put the widgets in order"""
        header.grid(row = 1, column= 0, columnspan = 5, sticky = 'n')
        subHeader.grid(row = 2, column = 0, columnspan = 5)
        boyBtn.grid(row = 3, column = 2)
        girlBtn.grid(row = 3, column = 3)
        submitBtn.grid(row = 5, column = 4)


######## The Main Home Page ########

class StartPage(tk.Frame):
   
    def __init__(self,master):
        headerFont = font.Font(family='Helvetica', size=20)
        """   this is the "main frame from tkinter """
        tk.Frame.__init__(self,master)
        """frmMain = tk.Frame(self,bg="blue")
        frmMain.grid(row = 0, column = 0, sticky = 'nesw')
        frmMain.grid_rowconfigure(0, weight=1)
        frmMain.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)"""
        """this is the label on the front page"""
        header = tk.Label(self, text="What Do You Want To Do Today? :)", font = headerFont)

       # """ This is for determining New Users, so allow the program to be more personalized"""

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
        
        
        
        
        """this is where I put the widgets in order"""
        header.grid(row = 1, column= 0, columnspan = 5, sticky = 'n')
        #header.grid_columnconfigure(5, weight = 2)
        #header.grid_rowconfigure(2, pad = 20, weight = 2)
        storyBtn.grid(row = 2, column = 0, pady = 20)
        gameBtn.grid(row = 2, column = 2, padx = 20)
        settingsBtn.grid(row = 2, column = 3, padx = 10)

######## Home page for Game selction ########

class GamePage(tk.Frame):
   
    def __init__(self,master):
        headerFont = font.Font(family='Helvetica', size=20)

        tk.Frame.__init__(self,master)
        tk.Label(self, text=emoji.emojize('Let\'s play some games!! \U0001F3AE 	'), font=headerFont).pack()
        colorBtn = tk.Button(self, text="Learn Basic Colors", command=lambda: master.switch_frame(colorPage))

        colorBtn.pack()

######## Color Learning Game ########
def redSpeak():
    playsound("red.mp3")

def greenSpeak():
    playsound("green.mp3")

def blueSpeak():
    playsound("blue.mp3")

def blueDelay():
    playsound("1secblue.wav")



def callback(event):
        print ("clicked at", event.x, event.y)
        
        if 30 < event.x < 120:
            print("Red")
            top = tk.Toplevel()
            redFont = font.Font(family='Helvetica', size = 100, weight = 'bold')
            top.title("Red")
            tk.Label(top, text = "Red", fg = "Red", font = redFont).pack()
            #diagrams = tk.PhotoImage(file='Red.gif')
            #logolbl= tk.Label(top, image = diagrams).pack()
            btn = tk.Button(top, text="Back").pack()
            hearBtn = tk.Button(top, text = "Hear This Color", command = redSpeak, bg="Red").pack()
            redSpeak()

        if 150 < event.x <240 :
            print("Green")
            top = tk.Toplevel()
            greenFont = font.Font(family='Helvetica', size = 100, weight = 'bold')
            top.title("Green")
            tk.Label(top, text = "Green", fg = "Green", font = greenFont).pack()
            btn = tk.Button(top, text="Back").pack()
            hearBtn = tk.Button(top, text = "Hear This Color", command = greenSpeak, bg="Green").pack()
            greenSpeak()

        if 270 < event.x < 370:
            print("Blue")
            top = tk.Toplevel()
            blueFont = font.Font(family='Helvetica', size = 100, weight = 'bold')
            top.title("Blue")
            tk.Label(top, text = "Blue", fg = "Blue", font = blueFont).pack()
            btn = tk.Button(top, text="Back").pack()
            hearBtn = tk.Button(top, text = "Hear This Color", command = blueSpeak, bg="RoyalBlue").pack()
            if 'normal' == top.state():
                blueSpeak()
class colorPage(tk.Frame):

    def __init__(self,master):
        headerFont = font.Font(family='Helvetica', size = 20)
        tk.Frame.__init__(self,master)
        tk.Label(self, text="Tap the color to learn the name of it :)", font = headerFont).pack()

        canvas = tk.Canvas(self)  
        canvas.create_rectangle(30, 10, 120, 80,
            outline="Black", fill="Red")
        canvas.create_rectangle(150, 10, 240, 80,
            outline="Black", fill="Green")
        canvas.create_rectangle(270, 10, 370, 80,
            outline="Black", fill="Blue")
        canvas.focus_set()
        canvas.bind("<Button-1>", callback)
        canvas.pack()



######## Home page with the story interactions ########

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

######## One of the story interaction options ########

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

######## One of the story interaction options ########
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
    