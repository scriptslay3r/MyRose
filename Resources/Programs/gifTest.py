from tkinter import *
import time
import os
root = Tk()

there = os.path.abspath(os.curdir)
print(there)
filename = os.path.join(there, 'Resources', 'Images', 'Eyes.gif')

frames = [PhotoImage(file=filename,format = 'gif -index %i' %(i)) for i in range(100)]

def update(ind):

    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()