import pygame
from tkinter import *

# Colors
bgColor = "#323437"

def clicked():
    label.configure(text="I just got clicked")


if __name__ == "__main__":
    # Initialize window
    window = Tk()

    # Window settings
    windowSize = "900x500"
    window.title("TypeWriter")
    window["background"] = bgColor
    window.geometry(windowSize)

    label = Label(window, text="Hello World", background=bgColor)
    label.grid()



    window.mainloop()