from tkinter import *
from blankScreen import *

class EnrollScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: tuple):
        super().__init__(root, frame, screens)  
        enrollments = len([1,2,3])
        self.part_row1 = self.width/(9)
        place_rec = self.part_row1
        for i in range (4):
            self.canvas.create_rectangle(place_rec, self.height/8, place_rec+self.part_row1, self.height/2.5)
            label_name = Label(root,text="name")
            label_time = Label(root,text="time")
            label_date = Label(root,text="date")
            button_enroll = Button(root, text='enroll', command='')

            label_name.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+((self.height/2.5-self.height/8)/4))
            label_time.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+2*((self.height/2.5-self.height/8)/4))
            label_date.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+3*((self.height/2.5-self.height/8)/4))
            button_enroll.place()
            place_rec += (2*self.part_row1)

        place_rec = self.part_row1
        for i in range (enrollments-4):
            self.canvas.create_rectangle(place_rec, self.height-self.height/2.5, place_rec+self.part_row1, self.height-self.height/(8))
            place_rec += (2*self.part_row1)

    def get_enroll ():
        return [1,2,3]
