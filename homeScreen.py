from tkinter import *
from blankScreen import *

class HomeScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
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
        
        if self.usertype == "Student": # Student
             button_grades = Button(root,text="Grades",command = lambda: self.changeScreen("Grades")).place(x= (self.width/3), y= (self.height/3))
             button_schedule = Button(root,text="Schedule",command = lambda: self.changeScreen("Schedule")).place(x= (self.width/3*2), y= (self.height/3))
             button_profile = Button(root,text="Profile",command = lambda: self.changeScreen("Profile")).place(x= (self.width/3), y= (self.height/3*2))
             button_enroll = Button(root,text="Enroll",command = lambda: self.changeScreen("Enroll")).place(x= (self.width/3*2), y= (self.height/3*2))

        elif self.usertype == "Teacher": # Teacher
            button_subjects = Button(root,text="Subjects",command = lambda: self.changeScreen("Subject")).place(x= (self.width/3), y= (self.height/3))
            button_scheduleteacher = Button(root,text="Schedule",command = lambda: self.changeScreen("Schedule")).place(x= (self.width/3*2), y= (self.height/3))

        elif self.usertype == "Administrator": # Administrator
            button_student = Button(root,text="Student",command = lambda: self.changeScreen("AdminStudent")).place(x= (self.width/3), y= (self.height/3))
            button_teacher = Button(root,text="Teacher",command = lambda: self.changeScreen("AdminTeacher")).place(x= (self.width/3*2), y= (self.height/3))
            button_gradesadmin = Button(root,text="Grades",command = lambda: self.changeScreen("AdminGrades")).place(x= (self.width/3), y= (self.height/3*2))
            button_course = Button(root,text="Course",command = lambda: self.changeScreen("AdminCourse")).place(x= (self.width/3*2), y= (self.height/3*2))