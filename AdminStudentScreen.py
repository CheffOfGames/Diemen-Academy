from tkinter import *
from blankScreen import *
class AdminStudentScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)

        self.id_label = Label(self.frame,text="Student ID:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-5))
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-5))

        self.name_label = Label(self.frame,text="Student Name:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-4))
        self.name_entry = Entry(self.frame)
        self.name_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-4))

        self.lastname_label = Label(self.frame,text="Student Last Name:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-3))
        self.lastname_entry = Entry(self.frame)
        self.lastname_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-3))

        self.dob_label = Label(self.frame,text="Student Date of Birth:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.dob_entry = Entry(self.frame)
        self.dob_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        self.nat_label = Label(self.frame,text="Student Nationality:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.nat_entry = Entry(self.frame)
        self.nat_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.gender_label = Label(self.frame,text="Student Gender:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*0))
        self.gender_entry = Entry(self.frame)
        self.gender_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.email_label = Label(self.frame,text="Student Email:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*1))
        self.email_entry = Entry(self.frame)
        self.email_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.start_label = Label(self.frame,text="Student Start Year:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*2))
        self.start_entry = Entry(self.frame)
        self.start_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.couns_label = Label(self.frame,text="Student Study Counselor:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*3))
        self.couns_entry = Entry(self.frame)
        self.couns_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*3))

        self.study_label = Label(self.frame,text="Student Study:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*4))
        self.study_entry = Entry(self.frame)
        self.study_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*4))

        self.postalcode_label = Label(self.frame,text="Postalcode:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*5))
        self.postalcode_entry = Entry(self.frame)
        self.postalcode_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*5))

        self.street_label = Label(self.frame,text="Street:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*6))
        self.street_entry = Entry(self.frame)
        self.street_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*6))

        self.housenumber_label = Label(self.frame,text="Housenumber:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*7))
        self.housenumber_entry = Entry(self.frame)
        self.housenumber_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*7))

        self.city_label = Label(self.frame,text="City:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*8))
        self.city_entry = Entry(self.frame)
        self.city_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*8))

        self.phone_label = Label(self.frame,text="Phone:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*9))
        self.phone_entry = Entry(self.frame)
        self.phone_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*9))

        self.show_button = Button(root, text="show", command=lambda: self.show_info()).place(x=(self.width/5), y=(6*self.height/7), anchor='center')
        self.add_button = Button(root, text="add", command=lambda: self.addinfo()).place(x=(2*self.width/5), y=(6*self.height/7), anchor='center')
        self.delete_button = Button(root, text="delete", command=lambda: self.delete_info()).place(x=(3*self.width/5), y=(6*self.height/7), anchor='center')
   
    def delete_info(self):
        try:
            self.cursor.execute(f"delete from adress where id=(select fk_adress_id from student where id = {self.id_entry.get()})")
            self.cursor.execute(f"delete from student where id={self.id_entry.get()}")
            self.succes_label = Label(self.frame,text="Student succesfully deleted!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*11), anchor='center')
            self.database.commit()
        except:
            self.notsucces_label = Label(self.frame,text="Student can't be deleted, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*11), anchor='center')


    def show_info(self):
        self.cursor.execute(f"select id, study_name from study")
        infostudies = self.cursor.fetchall()
        for i in range (len(infostudies)):
            self.info_label= Label(self.frame, text=infostudies[i]).place(x=4*self.width/6, y=(self.height/2.5)+((self.height*0.034)*(-4+i)))
        try:
            for i in self.info_in_a_list:
                i.destroy
        except:
            self.info_in_a_list = []

        try:
            self.cursor.execute(f"select * from student a, adress b where a.id = {self.id_entry.get()} and a.fk_adress_id=b.id")
            info = self.cursor.fetchall()[0]
            for i in range (len(info)):
                self.info_label= Label(self.frame, text=info[i]).place(x=self.width/6, y=(self.height/2.5)+((self.height*0.034)*(-5+i)))
                self.info_in_a_list.append(self.info_label)
        except:
            self.notsucces_label = Label(self.frame,text="enter valid id, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*11), anchor='center')

    def addinfo(self):
            self.cursor.execute("select max(id) from adress")   
            adress_id = (self.cursor.fetchall())[0][0]+1
            try:
                self.cursor.execute(f"insert into adress\
                                        values({adress_id}, \
                                            \"{self.street_entry.get()}\", {self.housenumber_entry.get()},\
                                            \"{self.postalcode_entry.get()}\", \"{self.city_entry.get()}\", \"{self.phone_entry.get()}\")")

                self.cursor.execute(f"insert into student (first_name, last_name, date_of_birth, nationality, gender, email, start_year, studycounselor, fk_study_id, fk_adress_id)\
                                    values( \"{self.name_entry.get()}\", \"{self.lastname_entry.get()}\",\
                                    \"{self.dob_entry.get()}\", \"{self.nat_entry.get()}\", \"{self.gender_entry.get()}\",\
                                        \"{self.email_entry.get()}\", {self.start_entry.get()}, \"{self.couns_entry.get()}\",\
                                        {self.study_entry.get()}, {adress_id})")

                self.database.commit()

                self.succes_label = Label(self.frame,text="Student succesfully added!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*11), anchor='center')
            except:
                self.notsucces_label = Label(self.frame,text="Student can't be added, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*11), anchor='center')
