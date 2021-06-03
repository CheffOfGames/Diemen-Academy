from tkinter import *
from blankScreen import *
class AdminExamScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)

        self.id_label = Label(self.frame,text="ID:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.room_label = Label(self.frame,text="Room:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*0))
        self.room_entry = Entry(self.frame)
        self.room_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.resit_label = Label(self.frame,text="Resit:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*1))
        self.resit_entry = Entry(self.frame)
        self.resit_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.date_label = Label(self.frame,text="Date (year-month-day):").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*2))
        self.date_entry = Entry(self.frame)
        self.date_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.start_label = Label(self.frame,text="Starts at:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*3))
        self.start_entry = Entry(self.frame)
        self.start_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*3))

        self.end_label = Label(self.frame,text="Ends at:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*4))
        self.end_entry = Entry(self.frame)
        self.end_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*4))

        self.course_label = Label(self.frame,text="Course:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*5))
        self.course_entry = Entry(self.frame)
        self.course_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*5))

        self.show_button = Button(root, text="show", command=lambda: self.show_info()).place(x=(self.width/5), y=(6*self.height/7), anchor='center')
        self.add_button = Button(root, text="add", command=lambda: self.submitgrade_info()).place(x=(2*self.width/5), y=(6*self.height/7), anchor='center')
        self.delete_button = Button(root, text="delete", command=lambda: self.delete_info()).place(x=(3*self.width/5), y=(6*self.height/7), anchor='center')
   
    def delete_info(self):
        try:
            self.cursor.execute(f"delete from exam where id={self.id_entry.get()}")
            self.succes_label = Label(self.frame,text="Grade succesfully deleted!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
            self.database.commit()
        except:
            self.notsucces_label = Label(self.frame,text="Grade can't be deleted, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')


    def show_info(self):
        self.cursor.execute(f"select a.id, a.course_name, b.resit from course a, exam b where b.fk_course_id = a.id;")
        infostudies = self.cursor.fetchall()
        for i in range (len(infostudies)):
            self.info_label= Label(self.frame, text=infostudies[i]).place(x=4*self.width/6, y=(self.height/2.5)+((self.height*0.034)*(-4+i)))
        
    def submitgrade_info(self):
        try:
            self.cursor.execute(f"insert into exam ( room, resit, date, starts_at, ends_at, fk_course_id)\
                                values(\'{self.room_entry.get()}\', {self.resit_entry.get()},\
                                    \'{self.date_entry.get()}\', \'{self.start_entry.get()}\', \'{self.end_entry.get()}\', {self.course_entry.get()})")
            self.database.commit()
            self.succes_label = Label(self.frame,text="Exam succesfully added!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
        except:
            self.notsucces_label = Label(self.frame,text="Exam can't be added, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')