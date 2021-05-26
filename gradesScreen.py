from tkinter import *
from blankScreen import *

class GradesScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: dict, database):
        super().__init__(root, frame, screens, database)
        self.root.title("Grades Screen")
        exams = [1,2,3,4,5]
        place = self.height/6
        for i in range (len(exams)):
            if i%2 == 0:
                self.canvas.create_rectangle(-1,place-self.height/20,self.width+1,place+self.height/20, fill="light grey", outline="")
            label_subject = Label(root,text="subject")
            label_subject.config(font=("Courier", 12))
            label_subject.place(x=self.width/12, y=place,anchor="center"  )

            label_grade = Label(root,text="grade")
            label_grade.config(font=("Courier", 12))
            label_grade.place(x=self.width/2, y=place,anchor="center"   )
            self.canvas.create_oval((self.width/2)-self.height/24, place-self.height/24,(self.width/2)+self.height/24, place+self.height/24)

            label_date = Label(root,text="date")
            label_date.config(font=("Courier", 12))
            label_date.place(x=9*self.width/10, y=place,anchor="center"  )

            place += self.height/10

