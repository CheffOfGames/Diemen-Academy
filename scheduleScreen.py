from tkinter import *
from blankScreen import *

class ScheduleScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: tuple):
        super().__init__(root, frame, screens)