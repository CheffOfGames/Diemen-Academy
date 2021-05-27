from tkinter import *
from blankScreen import *

class ProfileScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database):
        super().__init__(root, screens, database)  
        self.root.title("Profile Screen")
        self.label = Label(self.root, text="Name \nLast Name \nAdres")
        self.label.place(x =(self.width/4) , y= (self.height/7))
        self.canvas.create_rectangle((self.width/15), (self.height/7), (self.width/6), (self.height/2.5))
        