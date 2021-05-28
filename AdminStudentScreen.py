
from tkinter import *
from blankScreen import *
class AdminStudentScreen(Screen):
    def _init_(self, root: Tk, screens: dict, database):
        super()._init_(root, screens, database)
        
        self.id_label = Label(root,text="Student Number:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-5))
        self.id_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-5))

        self.name_label = Label(root,text="Student Name:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-4))
        self.name_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-4))

        self.lastname_label = Label(root,text="Student Last Name:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-3))
        self.lastname_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-3))

        self.dob_label = Label(root,text="Student Date of Birth:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.dob_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        self.nat_label = Label(root,text="Student Nationality:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.nat_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.gender_label = Label(root,text="Student Gender:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*0))
        self.gender_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.email_label = Label(root,text="Student Email:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*1))
        self.email_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.start_label = Label(root,text="Student Start Year:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))
        self.start_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.couns_label = Label(root,text="Student Study Counselor:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*3))
        self.couns_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*3))

        self.study_label = Label(root,text="Student Study:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*4))
        self.study_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*4))

        self.adress_label = Label(root,text="Student Adress:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*5))
        self.adress_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*5))

        #adding stuff to list
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

        self.frame_objects.append(self.email_label)
        self.frame_objects.append(self.email_entry)

        self.frame_objects.append(self.start_label)
        self.frame_objects.append(self.start_entry)

        self.frame_objects.append(self.couns_label)
        self.frame_objects.append(self.couns_entry)

        self.frame_objects.append(self.study_label)
        self.frame_objects.append(self.study_entry)

        self.frame_objects.append(self.adress_label)
        self.frame_objects.append(self.adress_entry)
