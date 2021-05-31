from tkinter import *
from blankScreen import *

class HomeScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        self.root.title("Home Screen")
        self.usertypes = {0: "Student", 1: "Teacher", 2: "Administrator"}
        try :
            self.usertype = self.usertypes[usertype]
        except KeyError :
            print("Unknown usertype.")
            self.changeScreen("Login")
        except :
            print("Something went wrong, please contact a System Administrator.")
            self.changeScreen("Login")
        
        if self.usertype == "Student": # Student
             button_grades = Button(root,text="Grades",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Grades")).place(x= (self.width/5*2), y= (self.height/3))
             button_schedule = Button(root,text="Schedule",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Schedule")).place(x= (self.width/5*4), y= (self.height/3))
             button_profile = Button(root,text="Profile",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Profile")).place(x= (self.width/5*2), y= (self.height/3*2))
             button_enroll = Button(root,text="Enroll",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Enroll")).place(x= (self.width/5*4), y= (self.height/3*2))

        elif self.usertype == "Teacher": # Teacher
            button_subjects = Button(root,text="Subjects",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Subject")).place(x= (self.width/5*2), y= (self.height/3))
            button_scheduleteacher = Button(root,text="Schedule",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Schedule")).place(x= (self.width/5*4), y= (self.height/3))

        elif self.usertype == "Administrator": # Administrator
            button_student = Button(root,text="Student",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("AdminStudent")).place(x= (self.width/5*2), y= (self.height/3))
            button_teacher = Button(root,text="Teacher",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("AdminTeacher")).place(x= (self.width/5*4), y= (self.height/3))
            button_gradesadmin = Button(root,text="Grades",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("AdminGrades")).place(x= (self.width/5*2), y= (self.height/3*2))
            button_course = Button(root,text="Course",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("AdminCourse")).place(x= (self.width/5*4), y= (self.height/3*2))