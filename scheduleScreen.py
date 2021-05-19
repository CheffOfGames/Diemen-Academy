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
        day = datetime.today()
        H = 0

        label_month = Label(root, text=str(calendar.month_name[day.month] ))
        label_month.config(font=("Courier", 12))
        label_month.place(x=self.width/2, y=self.height/8, anchor="center")
        for i in range (6):               #creates vertical lines
            self.canvas.create_line(i*place+2*place,self.height/6,i*place+2*place,18*self.height/20)
        for i in range (5): #[2.7*self.height/9, 4.2*self.height/9, 5.7*self.height/9, 7.2*self.height/9]: #creates horizontal lines
            self.canvas.create_line(place,(2.5+i*1.2)*self.height/9,place*8,(2.5+i*1.2)*self.height/9)

        days_of_the_month = calendar.monthrange(day.year, day.month)
        place = self.part_row1*(date(day.year, day.month, 1).weekday()+1)
        for i in range (days_of_the_month[1]):
            label_number = Label(root, text=str(i+1))
            label_number.place(x=place+(.05*self.part_row1), y=(self.height/8)+((self.height/2.5-self.height/8)/7)+H)
            # self.canvas.create_rectangle(place, self.height/6+ H, place+self.part_row1, self.height/3.8+ H)
            label_name = Label(root,text="subject")
            label_time = Label(root,text="date")
            label_date = Label(root,text="time")

            label_name.place(x=(place+(.25*self.part_row1)), y=(self.height/8)+((self.height/2.5-self.height/8)/7)+H)
            label_time.place(x=(place+(.25*self.part_row1)), y=(self.height/8)+1.7*((self.height/2.5-self.height/8)/7)+H)
            label_date.place(x=(place+(.25*self.part_row1)), y=(self.height/8)+2.5*((self.height/2.5-self.height/8)/7)+H)
            place += (self.part_row1)

            if (1+i+date(day.year, day.month, 1).weekday())%7 == 0:
                place = self.part_row1
                H += self.height/7.5
