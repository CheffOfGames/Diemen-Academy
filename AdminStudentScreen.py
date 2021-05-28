from tkinter import *
from blankScreen import *
class AdminStudentScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        
        self.id_label = Label(self.frame,text="Student Number:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-5))
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-5))

        self.name_label = Label(self.frame,text="Student Name:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-4))
        self.user_entry = Entry(self.frame)
        self.name_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-4))

        self.lastname_label = Label(self.frame,text="Student Last Name:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-3))
        self.lastname_entry = Entry(self.frame)
        self.lastname_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-3))

        self.dob_label = Label(self.frame,text="Student Date of Birth:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.dob_entry = Entry(self.frame)
        self.dob_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        self.nat_label = Label(self.frame,text="Student Nationality:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.nat_entry = Entry(self.frame)
        self.nat_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.gender_label = Label(self.frame,text="Student Gender:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*0))
        self.gender_entry = Entry(self.frame)
        self.gender_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.email_label = Label(self.frame,text="Student Email:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*1))
        self.email_entry = Entry(self.frame)
        self.email_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.start_label = Label(self.frame,text="Student Start Year:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))
        self.start_entry = Entry(self.frame)
        self.start_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.couns_label = Label(self.frame,text="Student Study Counselor:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*3))
        self.couns_entry = Entry(self.frame)
        self.couns_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*3))

        self.study_label = Label(self.frame,text="Student Study:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*4))
        self.study_entry = Entry(self.frame)
        self.study_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*4))

        self.adress_label = Label(self.frame,text="Student Adress:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*5))
        self.adress_entry = Entry(self.frame)
        self.adress_entry.place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*5))