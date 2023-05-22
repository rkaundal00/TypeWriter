import pygame
from tkinter import *

# Colors
bgColor = "#323437"

def puncClicked():
    if puncButton.cget("fg") == "red":
        puncButton.config(fg="black")
    else:
        puncButton.config(fg="red")

def numbersClicked():
    if numbersButton.cget("fg") == "red":
        numbersButton.config(fg="black")
    else:
        numbersButton.config(fg="red")

# TODO: load text
def loadText():
    return "Here comes the text"


if __name__ == "__main__":
    # Initialize window
    window = Tk()

    # Window settings
    windowSize = "1200x800"
    window.title("TypeWriter")
    window["background"] = bgColor
    window.geometry(windowSize)

    # Select options
    topFrame = Frame(window, width=600, height=50, borderwidth=5, relief=GROOVE)
    topFrame.pack(side=TOP, pady=20)

    puncButton = Button(topFrame, text="Punctuation", fg="black", command=puncClicked)
    puncButton.pack(side=LEFT)
    numbersButton = Button(topFrame, text="Numbers", fg="black", command=numbersClicked)
    numbersButton.pack(side=LEFT, padx=(0, 10))

    timeButton = Button(topFrame, text="Time")
    timeButton.pack(side=LEFT)
    wordsButton = Button(topFrame, text="Words")
    wordsButton.pack(side=LEFT)
    quoteButton = Button(topFrame, text="Quote")
    quoteButton.pack(side=LEFT)
    zenButton = Button(topFrame, text="Zen")
    zenButton.pack(side=LEFT)
    customButton = Button(topFrame, text="Custom")
    customButton.pack(side=LEFT)

    # load text for writing
    writing = loadText()

    textFrame = Frame(window, width=600, height=400, borderwidth=5, relief=GROOVE)
    textFrame.pack()
    text = Text(textFrame)
    text.insert(END, writing)
    text.pack()
    

    window.mainloop()