from tkinter import *
from blankScreen import *

class LoginScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: tuple):
        super().__init__(root, frame, screens)
        self.canvas.create_rectangle((self.width/2.3), (self.height/3), (self.width/1.7), (self.height/2))

        self.entry1 = Entry(root)
        self.entry2 = Entry(root)
        label1 = Label(root,text="Student Number")
        label1.place(x=(self.width/2.3), y=(self.height/2.5))
        self.entry1.place(x=(self.width/2), y=(self.height/2.5))

        label2 = Label(root,text="Password")
        label2.place(x=(self.width/2.3),y= (self.height/2.3))
        self.entry2.place(x=(self.width/2), y=(self.height/2.3))