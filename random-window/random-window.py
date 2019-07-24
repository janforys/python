from tkinter import *
import random

# set and draw window ("w")
w = Tk()
w.title("Choose Button")
w.geometry("400x400")

# function
def SetButtons ():
    how_many_buttons = 3
    global buttons
    buttons = []
    # variable with button which wins
    good = random.randint(0, how_many_buttons-1)
    for i in range (how_many_buttons):
        # checks if we win
        if i == good:
            buttons.append(Button(w, text = "click here", command = Hitted))
        else:
            buttons.append(Button(w, text = "click here", command = Mishit))
    for i in buttons:
        # window filling manner
        i.pack(fill=BOTH, expand=YES)

# function
def Hitted ():
    for i in buttons:
        i.destroy()
    global label
    # sets a label window with some text
    label = Label (w, text = "You chose RIGHT button")
    label.pack(fill=BOTH, expand=YES)
    w.after(2000, Restart)

def Mishit():
    for i in buttons:
        i.destroy()
    global label
    label = Label (w, text = "You chose WRONG button")
    label.pack(fill=BOTH, expand=YES)
    w.after(2000, Restart)

def Restart ():
    label.destroy()
    SetButtons()

SetButtons()


    
