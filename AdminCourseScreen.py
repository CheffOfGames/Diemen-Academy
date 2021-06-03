from tkinter import *
from blankScreen import *
class AdminCourseScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)

        self.name_label = Label(self.frame,text="Course Name:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.name_entry = Entry(self.frame)
        self.name_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.desc_label = Label(self.frame,text="Course Description:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*0))
        self.desc_entry = Entry(self.frame)
        self.desc_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.cred_label = Label(self.frame,text="Course Credits:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*1))
        self.cred_entry = Entry(self.frame)
        self.cred_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.teacher_label = Label(self.frame,text="Course Teacher:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*2))
        self.teacher_entry = Entry(self.frame)
        self.teacher_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.show_button = Button(root, text="show", command=lambda: self.show_info()).place(x=(self.width/5), y=(6*self.height/7), anchor='center')
        self.add_button = Button(root, text="add", command=lambda: self.submitcourse_info()).place(x=(2*self.width/5), y=(6*self.height/7), anchor='center')
        self.delete_button = Button(root, text="delete", command=lambda: self.delete_info()).place(x=(3*self.width/5), y=(6*self.height/7), anchor='center')
   
    def delete_info(self):
        try:
            self.cursor.execute(f"delete from course where id={self.id_entry.get()}")
            self.succes_label = Label(self.frame,text="Course succesfully deleted!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
            self.database.commit()
        except:
            self.notsucces_label = Label(self.frame,text="Course can't be deleted, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')


    def show_info(self):
        self.cursor.execute(f"select id, course_name from course")
        infostudies = self.cursor.fetchall()
        for i in range (len(infostudies)):
            self.info_label= Label(self.frame, text=infostudies[i]).place(x=4*self.width/6, y=(self.height/2.5)+((self.height*0.034)*(-4+i)))

    def submitcourse_info(self):
            self.cursor.execute("select max(id) from course")   
            course_id = (self.cursor.fetchall())[0][0]+1
            try:
                self.cursor.execute(f"insert into course\
                                        values({course_id}, \
                                            \"{self.name_entry.get()}\", \"{self.desc_entry.get()}\",\
                                            {self.cred_entry.get()}, {self.teacher_entry.get()})")

                self.database.commit()

                self.succes_label = Label(self.frame,text="Course succesfully added!", fg='green').place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
            except:
                self.notsucces_label = Label(self.frame,text="Course can't be added, please try again", fg='red').place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
