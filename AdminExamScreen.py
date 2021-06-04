from tkinter import *
from blankScreen import *
class AdminExamScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        # Set variables
        super().__init__(root, screens, database, user=user, usertype=usertype)

        # Create labels and entry fields for information necessary to add
        Label(self.frame,text="ID:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        Label(self.frame,text="Room:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*0))
        self.room_entry = Entry(self.frame)
        self.room_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        Label(self.frame,text="Resit:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*1))
        self.resit_entry = Entry(self.frame)
        self.resit_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        Label(self.frame,text="Date (year-month-day):").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*2))
        self.date_entry = Entry(self.frame)
        self.date_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        Label(self.frame,text="Starts at:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*3))
        self.start_entry = Entry(self.frame)
        self.start_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*3))

        Label(self.frame,text="Ends at:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*4))
        self.end_entry = Entry(self.frame)
        self.end_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*4))

        Label(self.frame,text="Course:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*5))
        self.course_entry = Entry(self.frame)
        self.course_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*5))

        # Add buttons to show, delete or create data
        Button(root, text="show", command=lambda: self.show_info()).place(x=(self.width/5), y=(6*self.height/7), anchor='center')
        Button(root, text="add", command=lambda: self.submit_exam_info()).place(x=(2*self.width/5), y=(6*self.height/7), anchor='center')
        Button(root, text="delete", command=lambda: self.delete_info()).place(x=(3*self.width/5), y=(6*self.height/7), anchor='center')
   
    def delete_info(self):
        # Try to delete data from exam, if it doesn't work, show error
        try:
            self.cursor.execute(f"delete from exam where id={self.id_entry.get()}")
            self.succes_label = Label(self.frame,text="Exam succesfully deleted!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
            self.database.commit()
        except:
            self.notsucces_label = Label(self.frame,text="Exam can't be deleted, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')


    def show_info(self):
        # If self.info_in_a_list exists, destroy it, otherwise create an empty list
        try:
            for i in self.info_in_a_list:
                i.destroy
        except:
            self.info_in_a_list = []

        # Try to get information about exam id, if it does not exist, give error message
        try:
            # Gather necessary information
            self.cursor.execute(f"select a.id, a.course_name, b.resit from course a, exam b where b.fk_course_id = a.id;")
            infostudies = self.cursor.fetchall()
            self.cursor.execute(f"select a.id,b.course_name from exam a, course b where a.fk_course_id=b.id")
            infoexams = self.cursor.fetchall()

            # For all information, print it
            for i in range (len(infostudies)):
                self.info_label= Label(self.frame, text=infostudies[i]).place(x=4*self.width/6, y=(self.height/2.5)+((self.height*0.034)*(-4+i)))
                self.info_in_a_list.append(i)
            for i in range(len(infoexams)):
                self.info_label= Label(self.frame, text=infoexams[i]).place(x=self.width/6, y=(self.height/2.5)+((self.height*0.034)*(-4+i)))
                self.info_in_a_list.append(i)
        except :
            Label(self.frame,text="enter valid id, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
    


    def submit_exam_info(self):
        # If possible, insert values, otherwise give error message
        try:
            # Enter information about the exam
            self.cursor.execute(f"insert into exam ( room, resit, date, starts_at, ends_at, fk_course_id)\
                                values(\'{self.room_entry.get()}\', {self.resit_entry.get()},\
                                    \'{self.date_entry.get()}\', \'{self.start_entry.get()}\', \'{self.end_entry.get()}\', {self.course_entry.get()})")

            # Commit changes
            self.database.commit()

            # Show success label
            Label(self.frame,text="Exam succesfully added!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
        except:
            Label(self.frame,text="Exam can't be added, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')