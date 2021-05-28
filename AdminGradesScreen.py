from tkinter import *
from blankScreen import *
class AdminGradesScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        
        self.id_label = Label(self.frame,text="Grade ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        self.grade_label = Label(self.frame,text="Grade:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.grade_entry = Entry(self.frame)
        self.grade_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.passed_label = Label(self.frame,text="Exam Passed?:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*0))
        self.passed_entry = Entry(self.frame)
        self.passed_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.student_label = Label(self.frame,text="Student ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*1))
        self.student_entry = Entry(self.frame)
        self.student_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.exam_label = Label(self.frame,text="Exam ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))
        self.exam_entry = Entry(self.frame)
        self.exam_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))