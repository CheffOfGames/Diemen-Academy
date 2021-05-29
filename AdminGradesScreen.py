from tkinter import *
from blankScreen import *
class AdminGradesScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)

        self.grade_label = Label(self.frame,text="Grade:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.grade_entry = Entry(self.frame)
        self.grade_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.passed_label = Label(self.frame,text="Exam Passed (0/1):").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*0))
        self.passed_entry = Entry(self.frame)
        self.passed_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.student_label = Label(self.frame,text="Student ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*1))
        self.student_entry = Entry(self.frame)
        self.student_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.exam_label = Label(self.frame,text="Exam ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))
        self.exam_entry = Entry(self.frame)
        self.exam_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.submitgrade_button = Button(root, text="Submit", command=lambda: self.submitgrade_info()).place(x=(self.width/2), y=(6*self.height/7), anchor='center')

    def submitgrade_info(self):
        try:
            self.cursor.execute(f"insert into result (grade, passed, fk_student_id, fk_exam_id)\
                                values({self.grade_entry.get()}, {self.passed_entry.get()},\
                                    {self.student_entry.get()}, {self.exam_entry.get()})")
            self.database.commit()
            self.succes_label = Label(self.frame,text="Grade succesfully added!", fg='green').place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))
        except:
            self.notsucces_label = Label(self.frame,text="Grade can't be added, please try again", fg='red').place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))