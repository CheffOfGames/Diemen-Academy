from tkinter import *
from blankScreen import *
class AdminGradesScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        # Set variables
        super().__init__(root, screens, database, user=user, usertype=usertype)

        # Create labels and entry fields for information necessary to add
        Label(self.frame,text="ID:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        Label(self.frame,text="Grade:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.grade_entry = Entry(self.frame)
        self.grade_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        Label(self.frame,text="Exam Passed (0/1):").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*0))
        self.passed_entry = Entry(self.frame)
        self.passed_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        Label(self.frame,text="Student ID:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*1))
        self.student_entry = Entry(self.frame)
        self.student_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        Label(self.frame,text="Exam ID:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*2))
        self.exam_entry = Entry(self.frame)
        self.exam_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        # Add buttons to show, delete or create data
        Button(root, text="show", command=lambda: self.show_info()).place(x=(self.width/5), y=(6*self.height/7), anchor='center')
        Button(root, text="add", command=lambda: self.submitgrade_info()).place(x=(2*self.width/5), y=(6*self.height/7), anchor='center')
        Button(root, text="delete", command=lambda: self.delete_info()).place(x=(3*self.width/5), y=(6*self.height/7), anchor='center')
   
    def delete_info(self):
        # Try to delete data from exam, if it doesn't work, show error
        try:
            self.cursor.execute(f"delete from grade where id={self.id_entry.get()}")
            self.succes_label = Label(self.frame,text="Grade succesfully deleted!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
            self.database.commit()
        except:
            self.notsucces_label = Label(self.frame,text="Grade can't be deleted, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')


    def show_info(self):
        # If self.info_in_a_list exists, destroy it, otherwise create an empty list
        try:
            for i in self.info_in_a_list:
                i.destroy
        except:
            self.info_in_a_list = []
            
        # Try to get information about grades, if it does not exist, give error message
        try: 
            # Gather necessary information
            self.cursor.execute(f"select a.id, b.course_name, a.resit from exam a, course b where a.fk_course_id = b.id;")
            infostudies = self.cursor.fetchall()

            # For all information, print it
            for i in range (len(infostudies)):
                self.info_label= Label(self.frame, text=infostudies[i]).place(x=4*self.width/6, y=(self.height/2.5)+((self.height*0.034)*(-4+i)))
                self.info_in_a_list.append(self.info_label)
        except:
            Label(self.frame,text="enter valid id, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')

    def submitgrade_info(self):
        # If possible, insert values, otherwise give error message
        try:
            # Enter information about the grades
            self.cursor.execute(f"insert into result (grade, passed, fk_student_id, fk_exam_id)\
                                values({self.grade_entry.get()}, {self.passed_entry.get()},\
                                    {self.student_entry.get()}, {self.exam_entry.get()})")

            # Commit changes
            self.database.commit()

            # Show success label
            self.succes_label = Label(self.frame,text="Grade succesfully added!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
        except:
            self.notsucces_label = Label(self.frame,text="Grade can't be added, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')