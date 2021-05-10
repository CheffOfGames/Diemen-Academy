from tkinter import *
from blankPage import *

class ProfileScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, canvas: Canvas, screens: set):
        super().__init__(root, frame, canvas, screens)