######## LOG ########
#####################
"""
Add Index to organize amount of #'s
Use CTR + F and copy and paste the #'s.
######## = LOG 
#######  = My Todo 

 ~ Tips ~

 Using this will change the size of the entire window.
 master.geometry("1250x10000")



June 2, 2020:
Add global counter the limit the amount of times the "Welcome" pop up box shows
Seperate COLORS into sections
I should had another step. Where it offers a Demo Option and a Setup Option. 

June 5, 2020:
Be more gender aware 
Maybe use "Parental Settings" 
Maybe use "You are so loved, instead of "Mommy and Daddy Love You"

"""
######## END LOG ########



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
from random import choice
from random import randint
from PIL import Image, ImageTk
from playsound import playsound
from time import sleep
from lib import fidgitSpinner
from lib import relaxingAutoPaint
from lib import youtubeAudioDownloader
from lib import AboutPage
## If Gender = 1, Gender = Boy
## If Gender = 2, Gender = Girl
global Gender

####### Button Styling #######
global btnRelief
btnRelief = 'groove'
global btnBorder
btnBorder = 10
#global btnFont
#btnFont = "(family = 'Helvetica', size = 15, weight = 'bold')"
global btnBG
btnBG = 'blue'
global fontFamily
fontFamily = 'Helvetica'
global fontSize
fontSize = 20 
global fontWeight
fontWeight = 'bold'
global btnWidth
btnWidth = 100
global btnHeight
btnHeight = 2
global btnPady
btnPady = 5
global btnPadx
btnPadx = 5
######## END Button Styling #########
global COLORS


#~~~~~~ I want to add a section to allow the user to disable certian colors ~~~~~ ###
def randomColor():
    COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
        'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
        'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
        'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
        'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
        'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
        'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
        'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
        'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
        'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
        'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
        'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
        'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
        'indian red', 'saddle brown', 'sandy brown',
        'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
        'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
        'pale violet red', 'maroon', 'medium violet red', 'violet red',
        'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
        'thistle', 'snow2', 'snow3',
        'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
        'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
        'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
        'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
        'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
        'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
        'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
        'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
        'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
        'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
        'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
        'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
        'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
        'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
        'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
        'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
        'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
        'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
        'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
        'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
        'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
        'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
        'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
        'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
        'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
        'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
        'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
        'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
        'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
        'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
        'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
        'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
        'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
        'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
        'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
        'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
        'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
        'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
        'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
        'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
        'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
        'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
        'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
        'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
        'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
        'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
        'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
        'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
        'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
        'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
        'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
        'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
        'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
        'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
        'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
        'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
        'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    BLUES = ['mint cream', 'azure', 'alice blue', 'lavender',
     'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'medium spring green', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4']

    global color
    color = choice(COLORS)
    global secondColor
    secondColor = choice(COLORS)
    global thirdColor
    thirdColor = choice(COLORS)
    global fourthColor 
    fourthColor = choice(COLORS)

    global randomBlue
    randomBlue = choice(BLUES)



babyName = "babyName.pckl" 
babyGender = "babyGender.pckl"
try:
    with open('babyName.pckl', 'rb') as b:
        baby = pickle.load(b)
except:
    pass
class myRose(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
       # btnFont = font.Font(family = 'Helvetica', size = 15, weight = 'bold')

        #here = os.path.dirname(os.path.abspath(__file__))
        
        #icon = os.path.join(here, 'rose.ico')
        self.title("Roses are red, violets are blue, No matter what, I will always love you")
        pix = self.winfo_height
        print(pix)     
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'Resources', 'Images', 'rose.gif')
        img = tk.PhotoImage(file= filename)

        self.tk.call('wm', 'iconphoto', self._w, img)
        #self.geometry("1200x1200")
       
        self._frame = None
       
        self.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)

        #~#~ Note To Self: Should I make ↓ a function?

        """This checks to see if the file babyGender.pckl exists. If the file does not exist,
        the file will be created. If it does exist, this means the program has ran before,
        becuase the program creates the file.
        I should had another step. Where it offers a Demo Option and a Setup Option."""

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
        self._frame.pack()
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

        

######## The Setup Page ########

class setup(tk.Frame):
   
    def __init__(self,master):
        headerFont = font.Font(family='Helvetica', size=20)
        subHeaderFont = font.Font(family='Helvetica', size=12)
        buttonFont = font.Font(family='Helvetica', size = 10, weight = 'bold')
        """   this is the "main frame from tkinter """
        tk.Frame.__init__(self,master = None)

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

            ##### Boy Selection #####

            if selection == 1:
                if not os.path.exists(babyGender):
                    with open ('babyGender.pckl', 'wb') as fGender:
                        pickle.dump("Boy", fGender)
                    name = simpledialog.askstring("Input", "Awwe, well congrats on your little boy! \nWhat is your son's name?")
                    with open('babyName.pckl', 'wb') as fName:
                        pickle.dump(name, fName)
                    
                    Gender = 1
                    tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)
                    master.switch_frame(StartPage)
                    ###### GO BACK AND DELETE THIS. FOR TESTING ONLY ##########

                    print(Gender)
                else:
                    with open('babyName.pckl', 'rb') as b:
                        baby = pickle.load(b)
                    #### Come Back And Add An Option to prompt if the user wants to continue anyway, deleting the old record
                    tk.messagebox.showwarning(title="Watch out now!!", message="It looks like you have already set up little baby " + baby)
                    MsgBox = tk.messagebox.askquestion ('Continue?','You can continue with the setup, it will delete ' + baby ,icon = 'warning')
                   
                    if MsgBox == 'yes':
                        with open('babyGender.pckl', 'wb') as fGender:
                            pickle.dump("Boy", fGender)
                        name = simpledialog.askstring("Input", "Awwe, well congrats on your little boy! \nWhat is your son's name?")
                        with open('babyName.pckl', 'wb') as fName:
                            pickle.dump(name, fName)
                        tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)

                        Gender = 1
                        master.switch_frame(StartPage)
                        ###### GO BACK AND DELETE THIS. FOR TESTING ONLY ##########

                        print(Gender)

           

            ##### Girl Selection #####
            elif selection == 2:
                if not os.path.exists(babyGender):
                    with open('babyGender.pckl', 'wb') as fGender:
                        pickle.dump("Girl", fGender)
                    name = simpledialog.askstring("Input", "Awwe, well congrats on your little girl! \nWhat is your daughter's name?")
                    with open('babyName.pckl', 'wb') as fName:
                        pickle.dump(name, fName)
                    tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)
                    Gender = 2
                    master.switch_frame(StartPage)

                    ###### GO BACK AND DELETE THIS. FOR TESTING ONLY ##########
                    print(Gender)
                else:
                    with open('babyName.pckl', 'rb') as b:
                        baby = pickle.load(b)
                    #### Come Back And Add An Option to prompt if the user wants to continue anyway, deleting the old record
                    tk.messagebox.showwarning(title="Watch out now!!", message="It looks like you have already set up little baby " + baby)
                    MsgBox = tk.messagebox.askquestion ('Continue?','You can continue with the setup, it will delete ' + baby ,icon = 'warning')
                    if MsgBox == 'yes':
                        with open('babyGender.pckl', 'wb') as fGender:
                            pickle.dump("Girl", fGender)
                        name = simpledialog.askstring("Input", "Awwe, well congrats on your little girl! \nWhat is your daughter's name?")
                        with open('babyName.pckl', 'wb') as fName:
                            pickle.dump(name, fName)
                        tk.messagebox.showinfo(title="Welcome!!", message="Mommy and Daddy love you " + name)
                        Gender = 2
                        master.switch_frame(StartPage)
            elif selection == 0:
                tk.messagebox.showwarning(title="Uh Oh! :/", message="Please make sure you selection something and try again :)")
            
            else:
                tk.messagebox.showwarning(title="Uh Oh! :/", message="Something went wrong :((")



        boyBtn = tk.Radiobutton(self, text = "A Baby Boy", variable = var, value = 1, indicatoron = 0, bg = "RoyalBlue", font = buttonFont)
        girlBtn = tk.Radiobutton(self, text = "A Baby Girl", variable = var, value = 2, indicatoron = 0, bg = "Pink", font = buttonFont )
        submitBtn = tk.Button(self, text = "Submit", command = submitButtons)
        """ Set up the personalization by adding baby's name"""
        boyBtn.config(relief = btnRelief, bd = btnBorder)
        girlBtn.config(relief = btnRelief, bd = btnBorder)
        submitBtn.config(relief = btnRelief, bd = btnBorder)

    
        
        
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
        #self.master.geometry("700x700")
        

        """this is the Header on the front page"""
        self.config(bg='white', height = 20000)
        self.pack(expand=1, fill="both")
        
        """
        
        secondFrame = tk.Frame(self)
		
        secondFrame.config(bg = 'blue', width = 1000, height = 2000)
               
        secondFrame.pack(side = "bottom")
        secondFrame.pack_propagate(True)
        
		#self.pack(in_secondFrame)
		"""
               
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'Resources', 'Images', 'header.png')
        
        
        
        image = Image.open(filename)
        image = image.resize((1200, 250), Image.ANTIALIAS) 
        photo = ImageTk.PhotoImage(image)
        photoLabel = tk.Label(self, image=photo)
        photoLabel.image = photo
        header = photoLabel
        header.config(bd = btnBorder)
		

     

        babyName = "babyName.pckl" 
        def welcome():
             
            messageFont = font.Font(family='Helvetica', size=15)
            with open('babyName.pckl', 'rb') as b:
                baby = pickle.load(b)
            
            
            top = tk.Toplevel()
            top.title('Welcome')
            tk.Message(top, text="Mommy and Daddy love you " + baby, font = messageFont, padx=20, pady=20).pack()
            top.after(2000, top.destroy)
        
        welcome()
        """
        k = 1 
        if k == 1 and welcomeCounter == 1:
            welcome()
            k =+ 2
"""
        """while welcomeCounter == 1:
            welcome()
            welcomeCounter += 2
"""
            
        btnFont = font.Font(family = fontFamily, size = fontSize, weight = fontWeight)
        randomColor()
        
        storyBtn = tk.Button(self, text="Story Time!", fg = color, bg = secondColor,
                    pady = btnPady, padx = btnPadx, command=lambda: master.switch_frame(StoryPage))
        storyBtn.config(width = btnWidth, height = btnHeight, relief = btnRelief, bd = btnBorder, font = btnFont)
        randomColor()

        gameBtn = tk.Button(self, text="Games! :)", fg = color, bg = secondColor,
                    pady = btnPady, padx = btnPadx, command=lambda: master.switch_frame(GamePage))
        gameBtn.config(width = btnWidth, height = btnHeight, relief = btnRelief, bd = btnBorder, font = btnFont)
        randomColor()
        settingsBtn = tk.Button(self, text = "Mommy and Daddy Settings", fg = color, bg = secondColor,
                     pady = btnPady, padx = btnPadx, command=lambda: master.switch_frame(SettingPage))             
        settingsBtn.config(width = btnWidth, height = btnHeight, relief = btnRelief, bd = btnBorder, font = btnFont)
        randomColor()
        quitBtn = tk.Button(self, text = "Quit", fg = color, bg = secondColor,
                    pady = btnPady, padx = btnPadx, command = lambda: self.quit())
        quitBtn.config(width = btnWidth, height = btnHeight, relief = btnRelief, bd = btnBorder, font = btnFont)
        
        ###### ADDING PICTURES TO BUTTONS ######## )
        """
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'Resources', 'Images', 'circle.png')
        circleBtn = tk.Button(self, text="I'm a circle!")
        image = Image.open(filename)
        photo = ImageTk.PhotoImage(image)
        photoLabel = tk.Label(self, image=photo)
        photoLabel.image = photo
        circleBtn.config(image= photo)
        """
        
        
        """this is where I put the widgets in order"""
        """header.grid(row = 1, column= 1, columnspan = 5, sticky = 'n', padx = 30)

        storyBtn.grid(row = 2, column = 2, pady = 20)
        gameBtn.grid(row = 2, column = 3, padx = 20)
        settingsBtn.grid(row = 2, column = 4, padx = 10)
"""
        header.pack( padx = btnPadx)
        storyBtn.pack(pady = btnPady, padx = btnPadx)
        gameBtn.pack(pady = btnPady, padx = btnPadx)
        settingsBtn.pack(pady = btnPady, padx = btnPadx)
        quitBtn.pack(pady = btnPady, padx = btnPadx)
        #circleBtn.grid(row= 3, column = 5, padx = 10)
        #hotoLabel.grid(row = 4, column = 6)

        ######## Global Menu Bar ########
        def makeMenu():


            def hello():
                print("Hello")      

            def about():
                AboutPage.do()
            menubar = tk.Menu(self)
            # create a pulldown menu, and add it to the menu bar
            filemenu = tk.Menu(menubar, tearoff=1)
            filemenu.add_command(label="Open", font=("Verdana", 14), command=hello)
            filemenu.add_separator()
            filemenu.add_command(label="Save", font=("Verdana", 14), command=hello)
            filemenu.add_separator()
            filemenu.add_command(label="Exit", font=("Verdana", 14), command=self.quit)
            menubar.add_cascade(label="File", font=("Verdana", 16), menu=filemenu)
			
            # create more pulldown menus
            separatorMenu= tk.Menu(menubar, tearoff = 0)
            editmenu = tk.Menu(menubar, tearoff=0)
            editmenu.add_command(label="Cut", font=("Verdana", 14), command=hello)
            editmenu.add_separator()
            editmenu.add_command(label="Copy", font=("Verdana", 14), command=hello)
            editmenu.add_separator()
            editmenu.add_command(label="Paste", font=("Verdana", 14), command=hello)
            menubar.add_cascade(label="Edit", font=("Verdana", 16), menu=editmenu)
            menubar.add_cascade(label="", menu=separatorMenu)

            helpmenu = tk.Menu(menubar, tearoff=0)
            helpmenu.add_command(label="About", font=("Verdana", 14), command=about)
            menubar.add_cascade(label="Help", font=("Verdana", 16), menu=helpmenu)

            # display the menu
            master.config(menu=menubar)
            
            ######## END Global Menu Bar ########
        makeMenu()


       
######## Home page for Settings ########
 
class SettingPage(tk.Frame):
   
    def __init__(self,master):
        headerFont = font.Font(family='Helvetica', size=20)
        b = open(babyName, 'rb')
        baby = pickle.load(b)
        tk.Frame.__init__(self,master)
        tk.Label(self, text=emoji.emojize('Settings for mom and dad! \U00002699	'), font=headerFont).pack()
        musicBtn = tk.Button(self, text="Download Music For " + baby, command=lambda: youtubeAudioDownloader.download())
        homeBtn = tk.Button(self, text = "Go Home", command =lambda: master.switch_frame(StartPage))
        musicBtn.pack()
        homeBtn.pack()
        musicBtn.config(relief = btnRelief, bd = btnBorder)
        homeBtn.config(relief = btnRelief, bd = btnBorder)

######## Home page for Game selection ########

class GamePage(tk.Frame):
   
    def __init__(self,master):
        headerFont = font.Font(family='Helvetica', size=20)

        tk.Frame.__init__(self,master)
       # tk.Label(self, text=emoji.emojize('Let\'s play some games!! \U0001F3AE 	'), font=headerFont).pack()
        colorBtn = tk.Button(self, text="Learn Basic Colors", command=lambda: master.switch_frame(colorPage))
        fidgitBtn = tk.Button(self, text = "Fidgit Spinner!!", command =lambda: fidgitSpinner.fidgit())
        paintBtn = tk.Button(self, text = "Relax, with some auto painting beauty :)", command = lambda: relaxingAutoPaint.paint() )
        homeBtn = tk.Button(self, text = "Go Home", command = lambda: master.switch_frame(StartPage))
        
        paintBtn.pack()
        colorBtn.pack()
        fidgitBtn.pack()
        homeBtn.pack()
        homeBtn.config(relief = btnRelief, bd = btnBorder)
        colorBtn.config(relief = btnRelief, bd = btnBorder)
        
######## Color Learning Game ########


class colorPage(tk.Frame):


    def __init__(self,master):
        def redSpeak():
            here = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(here, 'Resources', 'Sounds', 'red.mp3')
            playsound(filename)

        def greenSpeak():
            here = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(here, 'Resources', 'Sounds', 'green.mp3')
            playsound(filename)
        def blueSpeak():
            here = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(here, 'Resources', 'Sounds', 'blue.mp3')
            playsound(filename)
        

        headerFont = font.Font(family='Helvetica', size = 20)
        colorBtnFont = font.Font(family = 'Helvetica', size = 40, weight = 'bold')
        tk.Frame.__init__(self,master)
        headerLbl = tk.Label(self, text="Tap the color to learn the name of it :)", font = headerFont)
        tk.Frame(self, width=385, height=460, relief='raised', borderwidth=5)
          


      
        backBtn = tk.Button(self, text = "Go Back", command = lambda: master.switch_frame(GamePage))
        greenBtn = tk.Button(self, text = "Green", fg = "#04B404", font =  colorBtnFont, bg = "#04B404", activebackground = '#088A08', relief="raised", bd = 25, width = 5, height = 2, command = lambda: greenSpeak())
        blueBtn = tk.Button(self, text = "Blue", fg = "Blue", font = colorBtnFont, bg = "blue", activebackground = '#0404B4', relief="raised", bd = 25, width = 5, height = 2, command = lambda: blueSpeak())
        redBtn = tk.Button(self, text = "Red", fg = "Red", font = colorBtnFont, bg = "red", activebackground = '#DF0101', relief="raised", bd = 25, width = 5, height = 2, command = lambda: redSpeak())

        headerLbl.grid(row = 0, column = 2, columnspan = 1)
        greenBtn.grid(row = 1, column = 1)
        blueBtn.grid(row = 1, column = 2)
        redBtn.grid(row = 1, column = 3)
        backBtn.grid(row = 2, column = 2, pady = 10)



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
        homeBtn = tk.Button(self, text = "Go Home", command = lambda: master.switch_frame(StartPage))
        
        
        
        
        """this is where I put the buttons in order"""
        storyBox.grid(row = 2, column = 2)
        s.grid(row = 2, column = 2, sticky= 'e', ipady=50)
        boyBtn.grid(row = 4, column = 1)
        girlBtn.grid(row = 4, column = 2)
        settingsBtn.grid(row = 4, column = 4)
        homeBtn.grid(row = 4, column = 5)

######## One of the story interaction options ########

class astronautPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self,master)
        headerLbl = tk.Label(self, text="Alright, junior astronaut \nLet's go explore space!")
        #searchBtn = tk.Button(self, text="Search")
        
        headerLbl.pack(pady='5')
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'Resources', 'Images', 'astronaut.png')
        
        image = Image.open(filename)
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
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'Resources', 'Images', 'princess.png')
        
        image = Image.open(filename)
        photo = ImageTk.PhotoImage(image)
        photoLabel = tk.Label(self, image=photo)
        photoLabel.image = photo
        photoLabel.pack(side='right')
        #searchBtn.pack(pady='5'), '
        tk.Button(self, text="Go Home",
                    command=lambda: master.switch_frame(StoryPage)).pack()





        
if __name__ == "__main__":
    #checkName()
    app = myRose()
    app.mainloop()
    
