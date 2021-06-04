from tkinter import *
from blankScreen import *

class SubjectScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        self.root.title("Subject Screen")
        self.part_row1 = self.width/(9)
        place_rec = self.part_row1
        H = 0
        
        self.cursor.execute(f"select course_name, id from course where fk_teacher_id = {self.current_user}")
        subjects = self.cursor.fetchall()

        for i in range (len(subjects)):
            # self.canvas.create_rectangle(place_rec, self.height/8+ H, place_rec+self.part_row1, self.height/2.5+ H)
            self.label_name = Label(root,text=f"{subjects[i][0]}")
            self.label_name.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+((self.height/2.5-self.height/8)/4)+H)
            self.cursor.execute(f"select first_name, last_name from student, studycourse\
                                    where student.fk_study_id = studycourse.fk_study_id\
                                    and studycourse.fk_course_id in (select id from course where fk_teacher_id = {self.current_user} and id = {subjects[i][1]})")
            students = self.cursor.fetchall()
            temp = 1.5
            for i in students:
                self.label_students= Label(root, text=f"{i}")
                self.label_students.place(x=(place_rec+(.25*self.part_row1)), y=(self.height/8)+((self.height/2-self.height/8)/4)*temp+H)
                temp += 0.3

            
            # place_rec += (2*self.part_row1)

            while 4 == i and H == 0:
                place_rec = self.part_row1
                H = self.height/3

