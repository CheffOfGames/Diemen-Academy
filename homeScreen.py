from tkinter import *
from blankScreen import *

class HomeScreen(Screen):
    def __init__(self, root: Tk, frame: Frame, screens: tuple):
        super().__init__(root, frame, screens)
        self.usertypes = {0: "Student", 1: "Teacher", 2: "Administrator"}
        try :
            self.usertype = self.usertypes[user]
        except KeyError :
            # Switch back to login
            print("Unknown usertype.")
        except :
            # Switch back to login
            print("Something went wrong, please contact a System Administrator.")