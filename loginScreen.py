from tkinter import *
from blankScreen import *

class LoginScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database):
        super().__init__(root, screens, database)  
        self.canvas.create_rectangle((self.width/2.35), (self.height/2.75), (self.width/1.65), (self.height/1.9)) # Rect around login field
        self.root.title("Login Screen")

        # Enter username field
        self.user_label = Label(root,text="Student Number:").place(x=(self.width/2.31), y=(self.height/2.5))
        self.user_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.5))

        # Enter password field
        self.pass_label = Label(root,text="Password:").place(x=(self.width/2.31),y= (self.height/2.3))
        self.pass_entry = Entry(root).place(x=(self.width/2), y=(self.height/2.3))

        # Submit button
        self.login_button = Button(self.frame, text="Submit", command=lambda: self.login()).place(x=(self.width/2.05), y=(self.height/2.1))


        # Add frame objects to list
        self.frame_objects.append(self.user_label)
        self.frame_objects.append(self.user_entry)
        self.frame_objects.append(self.pass_label)
        self.frame_objects.append(self.pass_entry)
        self.frame_objects.append(self.login_button)

    def login(self):
        try: 
            self.current_user = self.user_entry.get()
        except:
            print("small error")
        self.changeScreen("Home")