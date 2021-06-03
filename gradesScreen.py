from tkinter import *
from blankScreen import *
import mysql.connector

class GradesScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        self.root.title("Grades Screen")
        place = self.height/6

        self.cursor.execute(f" select a.course_name, b.grade, b.passed, c.date, c.resit from course a, result b, exam c\
                                where b.fk_student_id = {self.current_user}\
                                and b.fk_exam_id = c.id\
                                and a.id = c.fk_course_id ") 
        exams = self.cursor.fetchall() 

        for i in range (len(exams)):
            if i%2 == 0:
                self.canvas.create_rectangle(-1,place-self.height/20,self.width+1,place+self.height/20, fill="light grey", outline="")
            exam = exams[i][0]
            if exams[i][4] == 1:
                exam += ' Resit'
            label_subject = Label(root,text=exam)
            label_subject.config(font=("Courier", 12))
            label_subject.place(x=self.width/20, y=place,anchor="w"  )

            if exams[i][2] == 0:
                label_grade = Label(root,text=exams[i][1], fg='red')
            else:
                label_grade = Label(root,text=exams[i][1])
                
            label_grade.config(font=("Courier", 12))
            label_grade.place(x=self.width/2, y=place,anchor="center"   )
            self.canvas.create_oval((self.width/2)-self.height/24, place-self.height/24,(self.width/2)+self.height/24, place+self.height/24)

            label_date = Label(root,text=exams[i][3])
            label_date.config(font=("Courier", 12))
            label_date.place(x=9*self.width/10, y=place,anchor="center"  )

            place += self.height/10

