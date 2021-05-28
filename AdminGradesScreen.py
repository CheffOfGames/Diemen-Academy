from tkinter import *
from blankScreen import *
class AdminGradesScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        
        self.id_label = Label(root,text="Grade ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.id_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        self.grade_label = Label(root,text="Grade:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.grade_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.passed_label = Label(root,text="Exam Passed?:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*0))
        self.passed_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.student_label = Label(root,text="Student ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*1))
        self.student_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.exam_label = Label(root,text="Exam ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))
        self.exam_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.frame_objects.append(self.id_label)
        self.frame_objects.append(self.id_entry)

        self.frame_objects.append(self.grade_label)
        self.frame_objects.append(self.grade_entry)

        self.frame_objects.append(self.passed_label)
        self.frame_objects.append(self.passed_entry)

        self.frame_objects.append(self.student_label)
        self.frame_objects.append(self.student_entry)

        self.frame_objects.append(self.exam_label)
        self.frame_objects.append(self.exam_entry)