from tkinter import *
from tkinter import messagebox

def button(name, mission,bg_color, fg_color, size):
    button = Button(text=name, command=mission, bg = bg_color, fg = fg_color,
                    font=('Neuropol Medium', 12), width=size)
    return button


def lable(name, bg_color, fg_color):
    label = Label(text=name, bg = bg_color , fg = fg_color, 
        font=('Univers Condensed Bold', 13))
    return label


def entry(win, size):
    txt = Entry(win, width=size, font=('Neuropol Medium', 11))
    return txt
