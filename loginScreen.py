from tkinter import *
from blankScreen import *

class LoginScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        super().__init__(root, screens, database, user=user, usertype=usertype)
        self.canvas.create_rectangle((self.width/2.75), (self.height/2.75), (self.width-self.width/2.75), (self.height/1.75)) # Rect around login field
        self.root.title("Login Screen")

        # Enter username field
        Label(root,text="Student Number:").place(x=(self.width/2.70), y=(self.height/2.5))
        self.user_entry = Entry(root)
        self.user_entry.place(x=(self.width/2), y=(self.height/2.5))

        # Enter password field
        Label(root,text="Password:").place(x=(self.width/2.70),y= (self.height/2.3))
        self.pass_entry = Entry(root, show="*")
        self.pass_entry.place(x=(self.width/2), y=(self.height/2.3))

        # Submit button
        self.login_button = Button(self.frame, text="Submit", command=lambda: self.login()).place(x=(self.width/2), y=(self.height/1.9), anchor='center')

    def login(self):
        # Grab username
        self.current_user = str(self.user_entry.get()).lower()

        
        # Check if teacher
        if self.current_user[0] == "t":
            # Try for errors while logging in
            try :
                # Remove the "t" from username to leave the id
                self.current_user = int(self.current_user[1:])

                # Grab the given id from the teacher table
                self.cursor.execute(f"select id from teacher where id={self.current_user}")
            except:
                self.error_popup("Please enter a real id")

            # Check if id exists
            if len(self.cursor.fetchall()) != 0 :
                try: 
                    # Grab data if id and password match
                    self.cursor.execute(f"select id from teacher where id={self.current_user} and password='{str(self.pass_entry.get())}'")

                    # Check if password exists
                    if len(self.cursor.fetchall()) != 0 :
                        # Set correct data and switch screens
                        self.current_usertype = 1
                        self.changeScreen("Home", self.current_usertype)
                    
                    # If there was a mistake, give error popup
                    else :
                        self.error_popup("Wrong password")
                except:
                    self.error_popup("Wrong password entered")
            else :
                self.error_popup("Please enter a real id")
            

        # Check for admin login and password (admin login is not in database thus has just a given password)
        elif self.current_user[0] == "a" and str(self.pass_entry.get()) == "root":
            # Set correct username, usertype and change screens
            self.current_user = self.current_user[1:]
            self.current_usertype = 2
            self.changeScreen("Home", self.current_usertype)
            
        # If not admin nor teacher, select student
        else:
            try:
                # Grab id if it is in student table
                self.cursor.execute(f"select id from student where id={self.current_user}")

                if len(self.cursor.fetchall()) != 0 :
                    # Grab data if id and password match
                    self.cursor.execute(f"select id from student where id={self.current_user} and password='{str(self.pass_entry.get())}'")

                    # Check if password exists
                    if len(self.cursor.fetchall()) != 0 :
                        # Set correct data and switch screens
                        self.current_usertype = 0
                        self.changeScreen("Home", self.current_usertype)
                    
                    # If there was a mistake, give error popup
                    else :
                        self.error_popup("Wrong password")
                else :
                    self.error_popup("Please enter a real id")
            except :
                self.error_popup("Please enter a real id")

    def error_popup(self, message) :
        print(message)
        # If error is thrown, empty the username and password entry fields
        self.user_entry.delete(0, 'end')
        self.pass_entry.delete(0, 'end')

        # Create new root
        error_root = Tk()
        error_root.resizable(0,0)
        error_root.title("ERROR")
        error_root.update()

        # Set location and size for error screen
        width, height = int(error_root.winfo_screenwidth()*.2), int(error_root.winfo_screenheight()*.2)
        error_root.geometry(f"{width}x{height}+{int((error_root.winfo_screenwidth()-width)/2)}+{int((error_root.winfo_screenheight()-height)/2)}")

        # Start frame, place error message and set button to return to main screen
        frame = Frame(error_root, width=width, height=height)
        Label(frame, text=f"{message}").place(x=width/2, y=height/2, anchor="center")
        Button(frame, text="Try again", command=lambda: error_root.destroy())