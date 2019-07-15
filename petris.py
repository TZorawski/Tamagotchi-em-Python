from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from itertools import count
import time
from random import *

class Application:
    def __init__(self, master, img, hei, wid):

        self.primeiroContainer = Canvas(master, height=hei, width=wid)
        self.primeiroContainer.pack()

        self.backStats = Label(self.primeiroContainer, height=10, width=700, bg='white')
        self.backStats.pack()

        self.backPicture = Label(self.primeiroContainer, height=690, width=1000, bg='#87cefa')
        self.backPicture.pack(fill=X)

        self.background_label = Label(self.backPicture, height=690, width=1000, image= img)
        self.background_label.place(x=0, y=0, relheight=1, relwidth=1)

    def load(self):
        im = 'jump.gif'
        if isinstance(im, str):
            im = Image.open(im)
        self.background_label.loc = 0
        self.background_label.frames = []

        try:
            for i in count(1):
                self.background_label.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.background_label.delay = im.info['duration']
        except:
            self.background_label.delay = 100

        if len(self.background_label.frames) == 1:
            self.background_label.config(image=self.background_label.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.background_label.config(image=None)
        self.background_label.frames = None

    def next_frame(self):
        if self.background_label.frames:
            self.background_label.loc += 1
            self.background_label.loc %= len(self.background_label.frames)
            self.background_label.config(image=self.background_label.frames[self.background_label.loc])
            self.background_label.after(self.background_label.delay, self.next_frame)

def image():
    a = PhotoImage(file='images/fat.gif')
    return a


root = Tk()
b = image()


Application(root, b, 1000, 1000)
root.mainloop()