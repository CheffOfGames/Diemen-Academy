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
        self.pass_entry = Entry(root, show="*")
        self.pass_entry.place(x=(self.width/2), y=(self.height/2.3))

        # Submit button
        self.login_button = Button(self.frame, text="Submit", command=lambda: self.login()).place(x=(self.width/2), y=(self.height/1.9), anchor='center')

    def login(self):
        self.current_user = str(self.user_entry.get()).lower()

        if self.current_user[0] == "t":
            try :
                self.current_user = int(self.current_user[1:])
                self.cursor.execute(f"select id from teacher where id={self.current_user}")

                if len(self.cursor.fetchall()) != 0 :
                    self.current_usertype = 1

                    self.cursor.execute(f"select id from teacher where id={self.current_user} and password={str(self.pass_entry.get())}")

                    if len(self.cursor.fetchall()) != 0 :
                        self.changeScreen("Home", self.current_usertype)
                    else :
                        self.error_popup("Wrong password")
                else :
                    self.error_popup("Please enter a real id")

            except :
                self.error_popup("Please enter a real id")

        elif self.current_user[0] == "a" and str(self.pass_entry.get()) == "root":
            self.current_user = self.current_user[1:]
            self.current_usertype = 2
            self.changeScreen("Home", self.current_usertype)
        
        else:
            try :
                self.cursor.execute(f"select id from student where id={self.current_user}")

                if len(self.cursor.fetchall()) != 0 :
                    self.current_usertype = 0

                    self.cursor.execute(f"select id from student where id={self.current_user} and password={str(self.pass_entry.get())}")

                    if len(self.cursor.fetchall()) != 0 :
                        self.changeScreen("Home", self.current_usertype)
                    else :
                        self.error_popup("Wrong password")
                else :
                    self.error_popup("Please enter a real id")
            except :
                self.error_popup("Please enter a real id")

    def error_popup(self, message) :
        self.user_entry.delete(0, 'end')
        self.pass_entry.delete(0, 'end')
        error_root = Tk()
        error_root.resizable(0,0)
        error_root.title("ERROR")
        width, height = int(error_root.winfo_screenwidth()*.2), int(error_root.winfo_screenheight()*.2)
        error_root.geometry(f"{width}x{height}+{int((error_root.winfo_screenwidth()-width)/2)}+{int((error_root.winfo_screenheight()-height)/2)}")
        frame = Frame(error_root, width=width, height=height)
        Label(frame, text=f"{message}").place(x=width/2, y=height/2, anchor="center")
        Button(frame, text="Try again", command=lambda: error_root.destroy())