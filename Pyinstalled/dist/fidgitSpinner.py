"""
Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.

"""

from turtle import *
import tkinter as tk
import tkinter.font as font
import pickle
def fidgit():
    state = {'turn': 0}

    def welcome():
        messageFont = font.Font(family='Helvetica', size=15)
        b = open('babyName.pckl', 'rb')
        baby = pickle.load(b)
        top = tk.Toplevel()
        top.title('Welcome')
        tk.Message(top, text="Alright " + baby + " Tap the Space Bar to spin the spinner!! :)", font = messageFont, padx=20, pady=20).pack()
        top.after(2000, top.destroy)

    def spinner():
        "Draw fidget spinner."
        clear()
        angle = state['turn'] / 10
        right(angle)
        forward(100)
        dot(120, 'red')
        back(100)
        right(120)
        forward(100)
        dot(120, 'green')
        back(100)
        right(120)
        forward(100)
        dot(120, 'blue')
        back(100)
        right(120)
        update()

    def animate():
        "Animate fidget spinner."
        if state['turn'] > 0:
            state['turn'] -= 1

        spinner()
        ontimer(animate, 20)

    def flick():
        "Flick fidget spinner."
        state['turn'] += 10

    setup(420, 420, 370, 0)
    hideturtle()
    welcome()
    tracer(False)
    width(20)
    onkey(flick, 'space')
    listen()
    animate()
    done()
