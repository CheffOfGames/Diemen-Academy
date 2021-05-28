from tkinter import *
from blankScreen import *
class AdminCourseScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)

        self.id_label = Label(self.frame,text="Course ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        self.name_label = Label(self.frame,text="Course Name:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.name_entry = Entry(self.frame)
        self.name_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.desc_label = Label(self.frame,text="Course Description:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*0))
        self.desc_entry = Entry(self.frame)
        self.desc_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.cred_label = Label(self.frame,text="Course Credits:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*1))
        self.cred_entry = Entry(self.frame)
        self.cred_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.teacher_label = Label(self.frame,text="Course Teacher:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))
        self.teacher_entry = Entry(self.frame)
        self.teacher_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))