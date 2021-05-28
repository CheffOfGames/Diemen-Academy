from tkinter import *
from blankScreen import *
class AdminTeacherScreen(Screen):
    def _init_(self, root: Tk, screens: dict, database):
        super()._init_(root, screens, database)
        
        self.id_label = Label(root,text="Teacher ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-4))
        self.id_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-4))

        self.name_label = Label(root,text="Teacher Name:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-3))
        self.name_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-3))

        self.lastname_label = Label(root,text="Teacher Last Name:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.lastname_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        self.dob_label = Label(root,text="Teacher Date of Birth:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.dob_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.nat_label = Label(root,text="Teacher Nationality:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*0))
        self.nat_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.gender_label = Label(root,text="Teacher Gender:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*1))
        self.gender_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.salary_label = Label(root,text="Teacher Salary:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))
        self.salary_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.couns_label = Label(root,text="Teacher Student Counselor:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*3))
        self.couns_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)((self.height*0.034)*3))

        self.adress_label = Label(root,text="Teacher Adress:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*4))
        self.adress_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*4))

        self.frame_objects.append(self.id_label)
        self.frame_objects.append(self.id_entry)

        self.frame_objects.append(self.name_label)
        self.frame_objects.append(self.name_entry)

        self.frame_objects.append(self.lastname_label)
        self.frame_objects.append(self.lastname_entry)

        self.frame_objects.append(self.dob_label)
        self.frame_objects.append(self.dob_entry)

        self.frame_objects.append(self.nat_label)
        self.frame_objects.append(self.nat_entry)

        self.frame_objects.append(self.gender_label)
        self.frame_objects.append(self.gender_entry)

        self.frame_objects.append(self.salary_label)
        self.frame_objects.append(self.salary_entry)

        self.frame_objects.append(self.couns_label)
        self.frame_objects.append(self.couns_entry)

        self.frame_objects.append(self.adress_label)
        self.frame_objects.append(self.adresss_entry)
