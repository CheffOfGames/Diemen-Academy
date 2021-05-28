from tkinter import *
from blankScreen import *
class AdminCourseScreen(Screen):
    def _init_(self, root: Tk, screens: dict, database):
        super()._init_(root, screens, database)

        self.id_label = Label(root,text="Course ID:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-2))
        self.id_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-2))

        self.name_label = Label(root,text="Course Name:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*-1))
        self.name_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*-1))

        self.desc_label = Label(root,text="Course Description:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*0))
        self.desc_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*0))

        self.cred_label = Label(root,text="Course Credits:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*1))
        self.cred_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*1))

        self.teacher_label = Label(root,text="Course Teacher:").place(x=(self.width/2.31), y=(self.height/2.5)+((self.height*0.034)*2))
        self.teacher_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5)+((self.height*0.034)*2))

        self.frame_objects.append(self.id_label)
        self.frame_objects.append(self.id_entry)

        self.frame_objects.append(self.name_label)
        self.frame_objects.append(self.name_entry)

        self.frame_objects.append(self.desc_label)
        self.frame_objects.append(self.desc_entry)

        self.frame_objects.append(self.cred_label)
        self.frame_objects.append(self.cred_entry)

        self.frame_objects.append(self.teacher_label)
        self.frame_objects.append(self.teacher_entry)