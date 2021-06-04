import calendar
from tkinter import *
from blankScreen import *
from datetime import *
from calendar import monthrange

class ScheduleScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        # Set variables
        super().__init__(root, screens, database, user=user, usertype=usertype)
        self.root.title("Schedule Screen")
        self.part_row1 = self.width/9
        self.place = self.part_row1
        self.day = date.today()
        self.H = 0

        # Create vertical lines
        for i in range (6):
            self.canvas.create_line(i*self.place+2*self.place,self.height/6,i*self.place+2*self.place,18*self.height/20)
        # Create horizontal lines
        for i in range (5): 
            self.canvas.create_line(self.place,(2.5+i*1.2)*self.height/9,self.place*8,(2.5+i*1.2)*self.height/9)

        # Set buttons to switch months
        Button(root, text=">", command=lambda: self.change_month(1)).place(x=19*self.width/20, y=self.height/2)
        Button(root, text="<", command=lambda: self.change_month(-1)).place(x=self.width/20, y=self.height/2)

        self.show_month()

    def change_month(self, next_previous):
        # Modify current data to meet expectations
        new = self.day.month+next_previous
        newyear = self.day.year

        # Fix issues when going to previous or next year respectively
        if new == 0:
            new = 12
            newyear -= 1
        elif new == 13:
            new = 1
            newyear += 1

        # Change data
        self.day = self.day.replace(month=new, year=newyear)

        # Delete everything on screen and set variables to start
        for i in self.month_stuff:
            i.destroy()
        self.H = 0

        # Show new data
        self.show_month() 
    
    def show_month(self):
        # Start list for objects to be deleted when switching screens
        self.month_stuff = []

        # Show month name
        label_month = Label(self.root, text=f"{calendar.month_name[self.day.month]} {self.day.year}")
        label_month.config(font=("Courier", 12))
        label_month.place(x=self.width/2, y=self.height/8, anchor="center")

        # Gather data needed to be shown in the schedule
        self.cursor.execute(f"  select a.course_name, b.resit, b.date, b.starts_at, b.ends_at, b.room from course a, exam b, studycourse c\
                                where c.fk_study_id = (select fk_study_id from student where id={self.current_user})\
                                and a.id = c.fk_course_id\
                                and a.id=b.fk_course_id")
        self.exams = self.cursor.fetchall() 

        # Gather position for start of month
        self.days_of_the_month = calendar.monthrange(self.day.year, self.day.month)
        self.place = self.part_row1*(date(self.day.year, self.day.month, 1).weekday()+1)

        # Show data for each day of the month
        for j in range (self.days_of_the_month[1]):
            
            # Check if day has exam, if so, print that information
            for i in self.exams:
                if self.day.year == datetime.strptime(str(i[2]), '%Y-%m-%d').year and self.day.month == datetime.strptime(str(i[2]), '%Y-%m-%d').month and j+1 == datetime.strptime(str(i[2]), '%Y-%m-%d').day:
                    label_exam_data = Label(self.root,text=f"{i[0]} {i[1]}\n{i[3]}-{i[4]}\n{i[5]}")
                    label_exam_data.place(x=(self.place+(.1*self.part_row1)), y=(self.height/8)+((self.height/2-self.height/8)/7)+self.H)
            
            # Print date number
            label_number = Label(self.root, text=str(j+1))
            label_number.place(x=self.place+(.05*self.part_row1), y=(self.height/8)+((self.height/2.5-self.height/8)/7)+self.H)
            
            # Modify location
            self.place += (self.part_row1)
            if (1+j+date(self.day.year, self.day.month, 1).weekday())%7 == 0: 
                self.place = self.part_row1
                self.H += self.height/7.5

        # Add everything that will need to be deleted on month switch
        self.month_stuff.append(label_month)
        self.month_stuff.append(label_exam_data)
        self.month_stuff.append(label_number)