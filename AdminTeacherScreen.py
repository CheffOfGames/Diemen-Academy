from tkinter import *
from blankScreen import *
class AdminTeacherScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        # Set variables
        super().__init__(root, screens, database, user=user, usertype=usertype)

        # Create labels and entry fields for information necessary to add
        Label(self.frame,text="Teacher ID:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*-4))
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-4))

        Label(self.frame,text="Name:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*-3))
        self.name_entry = Entry(self.frame)
        self.name_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-3))

        Label(self.frame,text="Last Name:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.lastname_entry = Entry(self.frame)
        self.lastname_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        Label(self.frame,text="Date of Birth (year-month-day):").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.dob_entry = Entry(self.frame)
        self.dob_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        Label(self.frame,text="Nationality:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*0))
        self.nat_entry = Entry(self.frame)
        self.nat_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        Label(self.frame,text="Gender:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*1))
        self.gender_entry = Entry(self.frame)
        self.gender_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        Label(self.frame,text="Salary:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*2))
        self.salary_entry = Entry(self.frame)
        self.salary_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        Label(self.frame,text="Student Counselor (Y/N):").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*3))
        self.couns_entry = Entry(self.frame)
        self.couns_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*3))

        Label(self.frame,text="Postalcode:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*4))
        self.postalcode_entry = Entry(self.frame)
        self.postalcode_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*4))

        Label(self.frame,text="Street:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*5))
        self.street_entry = Entry(self.frame)
        self.street_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*5))

        Label(self.frame,text="Housenumber:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*6))
        self.housenumber_entry = Entry(self.frame)
        self.housenumber_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*6))

        Label(self.frame,text="City:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*7))
        self.city_entry = Entry(self.frame)
        self.city_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*7))

        Label(self.frame,text="Phone:").place(x=(self.width/3.3), y=(self.height/2.5)+((self.height*0.034)*8))
        self.phone_entry = Entry(self.frame)
        self.phone_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*8))
        
        # Add buttons to show, delete or create data
        Button(root, text="show", command=lambda: self.show_info()).place(x=(self.width/5), y=(6*self.height/7), anchor='center')
        Button(root, text="add", command=lambda: self.addinfo()).place(x=(2*self.width/5), y=(6*self.height/7), anchor='center')
        Button(root, text="delete", command=lambda: self.delete_info()).place(x=(3*self.width/5), y=(6*self.height/7), anchor='center')
    
    def delete_info(self):
        # Try to delete data from teacher, if it doesn't work, show error
        try:
            self.cursor.execute(f"delete from adress where id=(select fk_adress_id from teacher where id = {self.id_entry.get()})")
            self.cursor.execute(f"delete from teacher where id={self.id_entry.get()}")
            Label(self.frame,text="Teacher succesfully deleted!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
            self.database.commit()
        except:
            Label(self.frame,text="Teacher can't be deleted, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')


    def show_info(self):
        # If self.info_in_a_list exists, destroy it, otherwise create an empty list
        try:
            for i in self.info_in_a_list:
                i.destroy
        except:
            self.info_in_a_list = []

        # Try to get information about teacher id, if it does not exist, give error message
        try:
            # Gather necessary information
            self.cursor.execute(f"select * from teacher a, adress b where a.id = {self.id_entry.get()} and a.fk_adress_id=b.id")
            info = self.cursor.fetchall()[0]

            # For all information, print it
            for i in range (len(info)):
                self.info_label= Label(self.frame, text=info[i]).place(x=self.width/6, y=(self.height/2.5)+((self.height*0.034)*(-4+i)))
                self.info_in_a_list.append(self.info_label)
        except:
            Label(self.frame,text="enter valid id, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')


    def addinfo(self):
        # Gather highest id and +1 it to get new id
        self.cursor.execute("select max(id) from adress")
        adress_id = (self.cursor.fetchall())[0][0]+1

        # If possible, insert values, otherwise give error message
        try:
            # Enter address data
            self.cursor.execute(f"insert into adress\
                                    values({adress_id}, \
                                        \"{self.street_entry.get()}\", {self.housenumber_entry.get()},\
                                        \"{self.postalcode_entry.get()}\", \"{self.city_entry.get()}\", \"{self.phone_entry.get()}\")")

            # Enter student informationdata
            self.cursor.execute(f"insert into teacher (first_name, last_name, date_of_birth, nationality, gender, salary, study_counselor, fk_adress_id)\
                                values( \"{self.name_entry.get()}\", \"{self.lastname_entry.get()}\",\
                                    \"{self.dob_entry.get()}\", \"{self.nat_entry.get()}\", \"{self.gender_entry.get()}\",\
                                    \"{self.salary_entry.get()}\", \"{self.couns_entry.get()}\",\
                                    {adress_id})")

            # Commit changes
            self.database.commit()

            # Show success label
            Label(self.frame,text="Teacher succesfully added!", fg='green').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')
        except:
            Label(self.frame,text="Teacher can't be added, please try again", fg='red').place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*10), anchor='center')