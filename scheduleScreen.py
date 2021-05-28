import calendar
from tkinter import *
from blankScreen import *
from datetime import *
from calendar import monthrange

class ScheduleScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database):
        super().__init__(root, screens, database)  
        self.root.title("Schedule Screen")
        self.part_row1 = self.width/9
        self.place = self.part_row1
        self.day = date.today()
        self.H = 0

        
        for i in range (6):               #creates vertical lines
            self.canvas.create_line(i*self.place+2*self.place,self.height/6,i*self.place+2*self.place,18*self.height/20)
        for i in range (5): #[2.7*self.height/9, 4.2*self.height/9, 5.7*self.height/9, 7.2*self.height/9]: #creates horizontal lines
            self.canvas.create_line(self.place,(2.5+i*1.2)*self.height/9,self.place*8,(2.5+i*1.2)*self.height/9)

        button_next = Button(root, text=">", command=lambda: self.change_month(self.day.month, 1))
        button_next.place(x=19*self.width/20, y=self.height/2)
        button_previous = Button(root, text="<", command=lambda: self.change_month(self.day.month, -1))
        button_previous.place(x=self.width/20, y=self.height/2)

        self.show_month()

    def change_month(self, month, next_previous):
        new = month+next_previous
        if new == -1:
            new = 12
        self.day = self.day.replace(month=new)
        for i in self.month_stuff:
            i.destroy()
        self.H = 0
        self.show_month()
        return 
    
    def show_month(self):
        self.month_stuff = []
        label_month = Label(self.root, text=str(calendar.month_name[self.day.month] ))
        label_month.config(font=("Courier", 12))
        label_month.place(x=self.width/2, y=self.height/8, anchor="center")
        self.month_stuff.append(label_month)

        self.cursor.execute(f"  select a.course_name, b.resit, b.date, b.starts_at, b.ends_at, b.room from course a, exam b\
                                where a.id=b.fk_course_id") # where date > '2018-01-01';
        exams = self.cursor.fetchall() 

        self.days_of_the_month = calendar.monthrange(self.day.year, self.day.month)
        self.place = self.part_row1*(date(self.day.year, self.day.month, 1).weekday()+1)
        for i in range (self.days_of_the_month[1]):
            label_number = Label(self.root, text=str(i+1))
            label_number.place(x=self.place+(.05*self.part_row1), y=(self.height/8)+((self.height/2.5-self.height/8)/7)+self.H)
            self.month_stuff.append(label_number)

            # self.canvas.create_rectangle(place, self.height/6+ H, place+self.part_row1, self.height/3.8+ H)
            label_name_time_place = Label(self.root,text="subject\ndate\ntime")
            label_name_time_place.place(x=(self.place+(.25*self.part_row1)), y=(self.height/8)+((self.height/2.5-self.height/8)/7)+self.H)
            self.place += (self.part_row1)

            self.month_stuff.append(label_name_time_place)

            if (1+i+date(self.day.year, self.day.month, 1).weekday())%7 == 0:
                self.place = self.part_row1
                self.H += self.height/7.5