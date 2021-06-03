from tkinter import *
from blankScreen import *
class AdminGradesScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)

        self.grade_label = Label(self.frame,text="Grade:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.grade_entry = Entry(self.frame)
        self.grade_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.passed_label = Label(self.frame,text="Exam Passed (0/1):").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*0))
        self.passed_entry = Entry(self.frame)
        self.passed_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.student_label = Label(self.frame,text="Student ID:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*1))
        self.student_entry = Entry(self.frame)
        self.student_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.exam_label = Label(self.frame,text="Exam ID:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*2))
        self.exam_entry = Entry(self.frame)
        self.exam_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.show_button = Button(root, text="show", command=lambda: self.show_info()).place(x=(self.width/5), y=(6*self.height/7), anchor='center')
        self.add_button = Button(root, text="add", command=lambda: self.submitgrade_info()).place(x=(2*self.width/5), y=(6*self.height/7), anchor='center')
        self.delete_button = Button(root, text="delete", command=lambda: self.delete_info()).place(x=(3*self.width/5), y=(6*self.height/7), anchor='center')
   
    def delete_info(self):
        try:
            self.cursor.execute(f"delete from student where id={self.id_entry.get()}")
            self.succes_label = Label(self.frame,text="Grade succesfully deleted!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
            self.database.commit()
        except:
            self.notsucces_label = Label(self.frame,text="Grade can't be deleted, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')


    def show_info(self):
        self.cursor.execute(f"select a.id, b.course_name, a.resit from exam a, course b where a.fk_course_id = b.id;")
        infostudies = self.cursor.fetchall()
        for i in range (len(infostudies)):
            self.info_label= Label(self.frame, text=infostudies[i]).place(x=4*self.width/6, y=(self.height/2.5)+((self.height*0.034)*(-4+i)))
        
    def submitgrade_info(self):
        try:
            self.cursor.execute(f"insert into result (grade, passed, fk_student_id, fk_exam_id)\
                                values({self.grade_entry.get()}, {self.passed_entry.get()},\
                                    {self.student_entry.get()}, {self.exam_entry.get()})")
            self.database.commit()
            self.succes_label = Label(self.frame,text="Grade succesfully added!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
        except:
            self.notsucces_label = Label(self.frame,text="Grade can't be added, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')