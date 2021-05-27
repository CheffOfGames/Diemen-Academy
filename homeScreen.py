from tkinter import *
from blankScreen import *

class HomeScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user:int):
        super().__init__(root, screens, database)  
        self.root.title("Home Screen")
        self.usertypes = {0: "Student", 1: "Teacher", 2: "Administrator"}
        try :
            self.usertype = self.usertypes[user]
        except KeyError :
            print("Unknown usertype.")
            self.changeScreen("Login")
        except :
            print("Something went wrong, please contact a System Administrator.")
            self.changeScreen("Login")
        
        if self.usertype == 0: # Student
             button_grades = Button(root,text="Grades",command = '')
             button_schedule = Button(root,text="Schedule",command = '')
             button_profile = Button(root,text="Profile",command = '')
             button_enroll = Button(root,text="Grades",command = '')

             button_grades.place(x= (self.width/3), y= (self.height/3))
             button_schedule.place(x= (self.width/3*2), y= (self.height/3))
             button_profile.place(x= (self.width/3), y= (self.height/3*2))
             button_enroll.place(x= (self.width/3*2), y= (self.height/3*2))

        elif self.usertype == 1: # Teacher
            button_subjects = Button(root,text="Subjects",command = '')
            button_scheduleteacher = Button(root,text="Schedule",command = '')

            button_subjects.place(x= (self.width/3), y= (self.height/3))
            button_scheduleteacher.place(x= (self.width/3*2), y= (self.height/3))

        elif self.usertype == 2: # Administrator
            button_student = Button(root,text="Student",command = '')
            button_teacher = Button(root,text="Teacher",command = '')
            button_gradesadmin = Button(root,text="Grades",command = '')
            button_course = Button(root,text="Course",command = '')

            button_student.place(x= (self.width/3), y= (self.height/3))
            button_teacher.place(x= (self.width/3*2), y= (self.height/3))
            button_gradesadmin.place(x= (self.width/3), y= (self.height/3*2))
            button_course.place(x= (self.width/3*2), y= (self.height/3*2))