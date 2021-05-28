from tkinter import *
from blankScreen import *
class AdminTeacherScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        
        self.id_label = Label(root,text="Teacher ID:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-4))
        self.id_entry = Entry(root)
        self.id_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-4))

        self.name_label = Label(root,text="Name:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-3))
        self.name_entry = Entry(root)
        self.name_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-3))

        self.lastname_label = Label(root,text="Last Name:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.lastname_entry = Entry(root)
        self.lastname_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        self.dob_label = Label(root,text="Date of Birth:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.dob_entry = Entry(root)
        self.dob_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.nat_label = Label(root,text="Nationality:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*0))
        self.nat_entry = Entry(root)
        self.nat_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.gender_label = Label(root,text="Gender:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*1))
        self.gender_entry = Entry(root)
        self.gender_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.salary_label = Label(root,text="Salary:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*2))
        self.salary_entry = Entry(root)
        self.salary_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.couns_label = Label(root,text="Student Counselor (Y/N):").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*3))
        self.couns_entry = Entry(root)
        self.couns_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*3))

        self.postalcode_label = Label(root,text="Postalcode:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*4))
        self.postalcode_entry = Entry(root)
        self.postalcode_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*4))

        self.street_label = Label(root,text="Street:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*5))
        self.street_entry = Entry(root)
        self.street_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*5))

        self.housenumber_label = Label(root,text="Housenumber:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*6))
        self.housenumber_entry = Entry(root)
        self.housenumber_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*6))

        self.city_label = Label(root,text="City:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*7))
        self.city_entry = Entry(root)
        self.city_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*7))

        self.phone_label = Label(root,text="Phone:").place(x=(self.width/3), y=(self.height/2.5)+((self.height*0.034)*8))
        self.phone_entry = Entry(root)
        self.phone_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*8))

        self.submit_button = Button(root, text="Submit", command=lambda: self.submit_info()).place(x=(self.width/2), y=(6*self.height/7), anchor='center')
 
        self.frame_object.append(self.id_label)
        self.frame_object.append(self.id_entry)

        self.frame_object.append(self.name_label)
        self.frame_object.append(self.name_entry)

        self.frame_object.append(self.lastname_label)
        self.frame_object.append(self.lastname_entry)

        self.frame_object.append(self.dob_label)
        self.frame_object.append(self.dob_entry)

        self.frame_object.append(self.nat_label)
        self.frame_object.append(self.nat_entry)

        self.frame_object.append(self.gender_label)
        self.frame_object.append(self.gender_entry)

        self.frame_object.append(self.salary_label)
        self.frame_object.append(self.salary_entry)

        self.frame_object.append(self.couns_label)
        self.frame_object.append(self.couns_entry)

        self.frame_object.append(self.postalcode_label)
        self.frame_object.append(self.postalcode_entry)

        self.frame_object.append(self.street_label)
        self.frame_object.append(self.street_entry)

        self.frame_object.append(self.housenumber_label)
        self.frame_object.append(self.housenumber_entry)

        self.frame_object.append(self.city_label)
        self.frame_object.append(self.city_entry)

        self.frame_object.append(self.phone_label)
        self.frame_object.append(self.phone_entry)


    def submit_info(self):
        self.cursor.execute(f"insert into teacher\
                            values({self.id_entry.get()}, \"{self.name_entry.get()}\", \"{self.lastname_entry.get()}\",\
                                \"{self.dob_entry.get()}\", \"{self.nat_entry.get()}\", \"{self.gender_entry.get()}\",\
                                \"{self.salary_entry.get()}\", \"{self.couns_entry.get()}\",\
                                ((select id from adress order by 1 desc limit 1)+1)")
        self.cursor.execute(f"insert into adress\
                                values(((select id from adress order by 1 desc limit 1)+1), \
                                    \"{self.street_entry.get()}\", {self.housenumber_entry.get()}\
                                    \"{self.postalcode_entry.get()}\", \"{self.city_entry.get()}\", \"{self.phone_entry.get()}\")")