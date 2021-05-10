from tkinter import *
from typing import Set

class Screen:
    def __init__(self, root:Tk, frame:Frame, canvas:Canvas, screens:tuple):
        self.root = root
        self.frame = frame
        self.canvas = canvas
        self.screens = screens
        
        self.root.update()
        self.height = self.root.winfo_height()
        self.width = self.root.winfo_width()
        
        self.canvas.create_line(0, self.height/10, self.width, self.height/10)
    
    def changeScreen(self, screen:str):
        if screen not in self.screens :
            raise KeyError("This screen does not exist.")
        