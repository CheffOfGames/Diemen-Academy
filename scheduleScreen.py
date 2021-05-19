import calendar
from tkinter import *
from blankScreen import *
from datetime import *
from calendar import monthrange

class ScheduleScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: tuple):
        super().__init__(root, frame, screens)
        self.part_row1 = self.width/9
        place = self.part_row1
        today = datetime.today()
        H = 0

        label_month = Label(root, text=str(calendar.month_name[today.month] ))
        label_month.config(font=("Courier", 12))
        label_month.place(x=self.width/2, y=self.height/8, anchor="center")
        for i in [place*2.5,place*4.5,place*6.5]:
            self.canvas.create_line(i,self.height/6,i,18*self.height/20)
        for i in [2*self.height/8, 3.5*self.height/8, 5*self.height/8, 6.5*self.height/8]:
            self.canvas.create_line(place,i,place*8,i)

        days_of_the_month = calendar.monthrange(today.year, today.month)
        # datetime.datetime.today().weekday()
        for i in range (days_of_the_month[1]):
            self.canvas.create_rectangle(place, self.height/6+ H, place+self.part_row1, self.height/3.8+ H)
            label_name = Label(root,text="day")
            label_time = Label(root,text="class")
            label_date = Label(root,text="class")

            label_name.place(x=(place+(.25*self.part_row1)), y=(self.height/8)+((self.height/2.5-self.height/8)/6)+H)
            label_time.place(x=(place+(.25*self.part_row1)), y=(self.height/8)+1.6*((self.height/2.5-self.height/8)/6)+H)
            label_date.place(x=(place+(.25*self.part_row1)), y=(self.height/8)+2.2*((self.height/2.5-self.height/8)/6)+H)
            place += (2*self.part_row1)

            if i == 6 or i == 13 or i == 20  or i == 27 :
                place = self.part_row1
                H += self.height/6
