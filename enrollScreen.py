from tkinter import *
from blankScreen import *

class EnrollScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        self.root.title("Enroll Screen")
        enrollments = len([1,2,3,4,5,6,7,8])
        self.part_row1 = self.width/(9)
        place_rec = self.part_row1
        x=enrollments%4 if enrollments < 4 else 4
        for i in range (x):
            self.canvas.create_rectangle(place_rec, self.height/8, place_rec+self.part_row1, self.height/2.5)
            label_name = Label(root,text="name")
            label_name.config(font=("Courier", 15))
            label_time = Label(root,text="time")
            label_time.config(font=("Courier", 10))
            label_date = Label(root,text="date")
            label_date.config(font=("Courier", 10))
            button_enroll = Button(root, text='enroll', command='')
            button_enroll.config(font=("Courier", 10))

            label_name.place(x=(place_rec+(.1*self.part_row1)), y=(self.height/8)+0.3*((self.height/2.5-self.height/8)/4))
            label_time.place(x=(place_rec+(.1*self.part_row1)), y=(self.height/8)+1.5*((self.height/2.5-self.height/8)/4))
            label_date.place(x=(place_rec+(.1*self.part_row1)), y=(self.height/8)+2.3*((self.height/2.5-self.height/8)/4))
            button_enroll.place(x=(place_rec+(.1*self.part_row1)), y=(self.height/8)+3*((self.height/2.5-self.height/8)/4))
            place_rec += (2*self.part_row1)

        place_rec = self.part_row1
        for i in range (enrollments-4):
            self.canvas.create_rectangle(place_rec, self.height-self.height/2.5, place_rec+self.part_row1, self.height-self.height/(8))
            label_name = Label(root,text="name")
            label_name.config(font=("Courier", 15))
            label_time = Label(root,text="time")
            label_time.config(font=("Courier", 10))
            label_date = Label(root,text="date")
            label_date.config(font=("Courier", 10))
            button_enroll = Button(root, text='enroll', command='')
            button_enroll.config(font=("Courier", 10))

            label_name.place(x=(place_rec+(.1*self.part_row1)), y=(self.height-self.height/2.5)+0.3*((self.height/2.5-self.height/8)/4))
            label_time.place(x=(place_rec+(.1*self.part_row1)), y=(self.height-self.height/2.5)+1.5*((self.height/2.5-self.height/8)/4))
            label_date.place(x=(place_rec+(.1*self.part_row1)), y=(self.height-self.height/2.5)+2.3*((self.height/2.5-self.height/8)/4))
            button_enroll.place(x=(place_rec+(.1*self.part_row1)), y=(self.height-self.height/2.5)+3*((self.height/2.5-self.height/8)/4))
            place_rec += (2*self.part_row1)
            

    def get_enroll ():
        return [1,2,3]
