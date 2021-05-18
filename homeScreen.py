from tkinter import *
from blankScreen import *

class HomeScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: tuple, user: int):
        super().__init__(root, frame, screens)
        self.usertypes = {0: "Student", 1: "Teacher", 2: "Administrator"}
        try :
            self.usertype = self.usertypes[user]
        except KeyError :
            print("Unknown usertype.")
            self.changeScreen("Login")
        except :
            print("Something went wrong, please contact a System Administrator.")
            self.changeScreen("Login")
        
        if self.usertype == 0: # Student
            pass

        elif self.usertype == 1: # Teacher
            pass

        elif self.usertype == 2: # Administrator
            pass