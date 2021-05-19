from tkinter import *
from blankScreen import *

class ScheduleScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: tuple):
        super().__init__(root, frame, screens)
        self.part_row1 = self.width/(18)
        place_rec = self.part_row1
        H = 0
        for i in range (31):
            self.canvas.create_rectangle(place_rec, self.height/6+ H, place_rec+self.part_row1, self.height/3.8+ H)
            label_name = Label(root,text="day")
            label_time = Label(root,text="class")
            label_date = Label(root,text="class")

            label_name.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+((self.height/2.5-self.height/8)/6)+H)
            label_time.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+1.6*((self.height/2.5-self.height/8)/6)+H)
            label_date.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+2.2*((self.height/2.5-self.height/8)/6)+H)
            place_rec += (2*self.part_row1)

            if i == 6 or i == 13 or i == 20  or i == 27 :
                place_rec = self.part_row1
                H = H + self.height/6
