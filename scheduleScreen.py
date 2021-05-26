import calendar
from tkinter import *
from blankScreen import *
from datetime import *
from calendar import monthrange

class ScheduleScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: dict, database):
        super().__init__(root, frame, screens, database, database)
        self.root.title("Schedule Screen")
        self.part_row1 = self.width/9
        place = self.part_row1
        self.day = date.today()
        H = 0

        label_month = Label(root, text=str(calendar.month_name[self.day.month] ))
        label_month.config(font=("Courier", 12))
        label_month.place(x=self.width/2, y=self.height/8, anchor="center")
        for i in range (6):               #creates vertical lines
            self.canvas.create_line(i*place+2*place,self.height/6,i*place+2*place,18*self.height/20)
        for i in range (5): #[2.7*self.height/9, 4.2*self.height/9, 5.7*self.height/9, 7.2*self.height/9]: #creates horizontal lines
            self.canvas.create_line(place,(2.5+i*1.2)*self.height/9,place*8,(2.5+i*1.2)*self.height/9)

        button_next = Button(root, text=">", command=lambda: self.change_month(self.day.month, 1))
        button_next.place(x=19*self.width/20, y=self.height/2)
        button_previous = Button(root, text="<", command=lambda: self.change_month(self.day.month, -1))
        button_previous.place(x=self.width/20, y=self.height/2)


        self.days_of_the_month = calendar.monthrange(self.day.year, self.day.month)
        place = self.part_row1*(date(self.day.year, self.day.month, 1).weekday()+1)
        for i in range (self.days_of_the_month[1]):
            label_number = Label(root, text=str(i+1))
            label_number.place(x=place+(.05*self.part_row1), y=(self.height/8)+((self.height/2.5-self.height/8)/7)+H)
            # self.canvas.create_rectangle(place, self.height/6+ H, place+self.part_row1, self.height/3.8+ H)
            label_name_time_place = Label(root,text="subject\ndate\ntime")
            # label_time = Label(root,text="")
            # label_date = Label(root,text="time")

            label_name_time_place.place(x=(place+(.25*self.part_row1)), y=(self.height/8)+((self.height/2.5-self.height/8)/7)+H)
            # label_time.place(x=(place+(.25*self.part_row1)), y=(self.height/8)+1.7*((self.height/2.5-self.height/8)/7)+H)
            # label_date.place(x=(place+(.25*self.part_row1)), y=(self.height/8)+2.5*((self.height/2.5-self.height/8)/7)+H)
            place += (self.part_row1)

            if (1+i+date(self.day.year, self.day.month, 1).weekday())%7 == 0:
                place = self.part_row1
                H += self.height/7.5

    def change_month(self, month, next_previous):
        new = month+next_previous
        if new == -1:
            new = 12
        self.day = self.day.replace(month=new)
        print (self.day)
        return self.day