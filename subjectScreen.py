from tkinter import *
from blankScreen import *

class SubjectScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: dict, database):
        super().__init__(root, frame, screens, database)
        self.root.title("Subject Screen")
        self.part_row1 = self.width/(9)
        place_rec = self.part_row1
        H = 0
        for i in range (9):
            self.canvas.create_rectangle(place_rec, self.height/8+ H, place_rec+self.part_row1, self.height/2.5+ H)
            label_name = Label(root,text="subject name")
            label_time = Label(root,text="time")
            label_date = Label(root,text="day")

            label_name.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+((self.height/2.5-self.height/8)/4)+H)
            label_time.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+2*((self.height/2.5-self.height/8)/4)+H)
            label_date.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+3*((self.height/2.5-self.height/8)/4)+H)
            place_rec += (2*self.part_row1)

            while 4 == i and H == 0:
                place_rec = self.part_row1
                H = self.height/3

