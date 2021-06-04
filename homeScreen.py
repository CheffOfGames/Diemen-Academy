from tkinter import *
from blankScreen import *

class HomeScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        # Set variables
        super().__init__(root, screens, database, user=user, usertype=usertype)
        self.root.title("Home Screen")
        
        # Make sure the correct usertype is given along
        if self.current_usertype != usertype :
            self.logout()
        
        # Set objects on screen for students
        if self.current_usertype == 0: 
            # Set buttons to navigate to the correct screens
            button_grades = Button(root,text="Grades",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Grades")).place(x= (self.width/3), y= (self.height/3),anchor = 'center')
            button_schedule = Button(root,text="Schedule",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Schedule")).place(x= (self.width/3*2), y= (self.height/3),anchor = 'center')
            button_profile = Button(root,text="Profile",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Profile")).place(x= (self.width/2), y= (self.height/3*2),anchor = 'center')

        # Set objects on screen for teachers
        elif self.current_usertype == 1: 
            # Set buttons to navigate to the correct screens
            button_subjects = Button(root,text="Subjects",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Subject")).place(x= (self.width/3), y= (self.height/3),anchor = 'center')
            button_scheduleteacher = Button(root,text="Profile",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("Profile")).place(x= (self.width/3*2), y= (self.height/3),anchor = 'center')

        # Set objects on screen for administrators
        elif self.current_usertype == 2: 
            # Set buttons to navigate to the correct screens
            button_student = Button(root,text="Student",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("AdminStudent")).place(x= (self.width/3), y= (self.height/3),anchor = 'center')
            button_teacher = Button(root,text="Teacher",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("AdminTeacher")).place(x= (self.width/3*2), y= (self.height/3),anchor = 'center')
            button_gradesadmin = Button(root,text="Grades",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("AdminGrades")).place(x= (self.width/3), y= (self.height/3*2),anchor = 'center')
            button_course = Button(root,text="Course",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("AdminCourse")).place(x= (self.width/3*2), y= (self.height/3*2),anchor = 'center')
            button_student = Button(root,text="Exam",width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)),command = lambda: self.changeScreen("AdminExam")).place(x= (self.width/3*1.5), y= (self.height/3*1.5),anchor = 'center')