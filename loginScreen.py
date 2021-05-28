from tkinter import *
from blankScreen import *

class LoginScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        self.canvas.create_rectangle((self.width/2.75), (self.height/2.75), (self.width-self.width/2.75), (self.height/1.75)) # Rect around login field
        self.root.title("Login Screen")

        # Enter username field
        self.user_label = Label(root,text="Student Number:").place(x=(self.width/2.70), y=(self.height/2.5))
        self.user_entry = Entry(root)
        self.user_entry.place(x=(self.width/2), y=(self.height/2.5))

        # Enter password field
        self.pass_label = Label(root,text="Password:").place(x=(self.width/2.70),y= (self.height/2.3))
        self.pass_entry = Entry(root)
        self.pass_entry.place(x=(self.width/2), y=(self.height/2.3))

        # Submit button
        self.login_button = Button(self.frame, text="Submit", command=lambda: self.login()).place(x=(self.width/2), y=(self.height/1.9), anchor='center')

    def login(self):
        self.current_user = str(self.user_entry.get()).lower()
        if self.current_user == "teacher":
            self.current_usertype = 1
        elif self.current_user == "admin" or self.current_user == "administrator":
            self.current_usertype = 2
        else :
            self.current_usertype = 0

        # if self.database has self.current_user: 
        #     self.current_usertype = user_type

        self.changeScreen("Home", self.current_usertype)