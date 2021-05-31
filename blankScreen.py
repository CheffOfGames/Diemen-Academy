from tkinter import *
import mysql.connector

# Set base coloring
top_bar_color = "Red"
logo_background = "White"
button_background = "Blue"
background_color = "White"

class Screen:
    def __init__(self, root:Tk, screens:dict, database, user="", usertype:int=-1):
        # Set variables
        self.root, self.screens, self.database = root, screens, database
        self.current_user, self.current_usertype = user, usertype
        self.cursor = database.cursor()
        self.root.title("Blank Screen") # Change root title
        
        # Set height/width for frame
        self.root.update()
        self.height = self.root.winfo_height()
        self.width = self.root.winfo_width()

        # Start frame and canvas
        self.frame = Frame(self.root, width=self.width, height=self.height, bg=background_color)
        self.frame.pack()
        self.canvas = Canvas(self.frame, width=self.width, height=self.height)
        
        # Create basic layout
        self.canvas.create_rectangle(0, 0, self.width, (self.height/10), fill=top_bar_color)
        self.canvas.create_rectangle((self.width/50), (self.height/50), (self.width/5), (self.height/10 - self.height/50), fill=logo_background) # Logo

        # Create navigation buttons
        if type(self).__name__ != "LoginScreen" :
            logout_button = Button(self.frame, width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)), text="Log out", command=lambda: self.logout()).place(x=int(self.width - self.width/5), y=int(self.height/50))
            if type(self).__name__ != "HomeScreen" :
                home_button = Button(self.frame, width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)), text="Home", command=lambda: self.changeScreen("Home", user=self.current_usertype)).place(x=int(self.width - self.width/2.5), y=int(self.height/50))
        self.canvas.pack()

    def changeScreen(self, screen:str, user:int=0):
        if not self.screens.get(screen) :
            raise KeyError("This screen does not exist.")
        # Delete all objects on screen
        self.canvas.destroy()
        self.frame.destroy()
        # Navigation to home needs user, otherwise gives error
        if user != self.current_usertype :
            self.current_usertype = user
        self = self.screens[screen](self.root, self.screens, self.database, self.current_user, self.current_usertype)

    def logout(self) :
        # Forget user information and change screens
        self.current_user = ""
        self.current_usertype = -1
        self.changeScreen("Login", self.current_usertype)
