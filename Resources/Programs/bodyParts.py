import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import os


class myRose(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        
        self.title("Let's Learn Body Parts!")
        #here = os.path.dirname(os.path.abspath(__file__))
        os.chdir("./")
        there = os.path.abspath(os.curdir)
        filename = os.path.join(there, 'Resources', 'Images', 'rose.gif')
        img = tk.PhotoImage(file= filename)
        self.tk.call('wm', 'iconphoto', self._w, img)
        #self.geometry("550x100")
        self._frame = None
            ##### Come back and add the ability for the program to detect the pickle files. if no files, open Setup, else open StartPage
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
        print(os.curdir)
        os.chdir("./")
        there = os.path.abspath(os.curdir)
        print(there)
        filename = os.path.join(there, 'Resources', 'Images', 'minion.gif')


        frames = [PhotoImage(file='mygif.gif',format = 'gif -index %i' %(i)) for i in range(100)]

        def update(ind):

            frame = frames[ind]
            ind += 1
            tk.Label.configure(image=frame)
            .after(100, update, ind)    
                
        """this is the label on the front page"""
        header = tk.Label(self, text="Tap the body part to hear it's name! :)", font = headerFont)



       # """ This is for determining New Users, so allow the program to be more personalized"""
        header.pack()


if __name__ == "__main__":
    #checkName()
    app = myRose()
    app.mainloop()

