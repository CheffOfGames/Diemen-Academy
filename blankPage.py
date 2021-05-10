from tkinter import *
from typing import Set

top_bar_color = "Red"
logo_background = "White"
button_background = "Blue"

class Screen:
    def __init__(self, root:Tk, frame:Frame, canvas:Canvas, screens:tuple):
        self.root = root
        self.frame = frame
        self.canvas = canvas
        self.screens = screens

        self.root.title("Blank Screen")
        
        self.root.update()
        self.height = self.root.winfo_height()
        self.width = self.root.winfo_width()
        
        self.canvas.create_rectangle(0, 0, self.width, (self.height/10), fill=top_bar_color)
        self.canvas.create_rectangle((self.width/50), (self.height/50), (self.width/5), (self.height/10 - self.height/50), fill=logo_background) # Logo
        self.canvas.create_rectangle((self.width - self.width/5), (self.height/50), (self.width - self.width/50), (self.height/10-self.height/50), fill=button_background)
    
    def changeScreen(self, screen:str):
        if screen not in self.screens :
            raise KeyError("This screen does not exist.")
        