from tkinter import *
from blankScreen import *
class AdminCourseScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)

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

        self.submit_button = Button(root, text="Submit", command=lambda: self.submitcourse_info()).place(x=(self.width/2), y=(6*self.height/7), anchor='center')


    def submitcourse_info(self):
            self.cursor.execute("select max(id) from course")   
            course_id = (self.cursor.fetchall())[0][0]+1
            try:
                self.cursor.execute(f"insert into course\
                                        values({course_id}, \
                                            \"{self.name_entry.get()}\", \"{self.desc_entry.get()}\",\
                                            {self.cred_entry.get()}, {self.teacher_entry.get()})")

                self.database.commit()

                self.succes_label = Label(self.frame,text="Course succesfully added!", fg='green').place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*4), anchor='center')
            except:
                self.notsucces_label = Label(self.frame,text="Course can't be added, please try again", fg='red').place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*4), anchor='center')
