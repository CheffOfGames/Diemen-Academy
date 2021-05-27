from tkinter import *

top_bar_color = "Red"
logo_background = "White"
button_background = "Blue"
background_color = "White"

class Screen:
    def __init__(self, root:Tk, screens:dict, database):
        self.root = root
        self.screens = screens
        self.database = database
        self.frame_objects = []
        self.current_user = ""

        self.root.title("Blank Screen")
        
        self.root.update()
        self.height = self.root.winfo_height()
        self.width = self.root.winfo_width()
        self.frame = Frame(self.root, width=self.width, height=self.height, bg=background_color)
        self.frame.pack()
        self.canvas = Canvas(self.frame, width=self.width, height=self.height)
        
        self.canvas.create_rectangle(0, 0, self.width, (self.height/10), fill=top_bar_color)
        self.canvas.create_rectangle((self.width/50), (self.height/50), (self.width/5), (self.height/10 - self.height/50), fill=logo_background) # Logo
        if type(self).__name__ != "LoginScreen" :
            logout_button = Button(self.frame, width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)), text="Log out", command=lambda: self.logout()).place(x=int(self.width - self.width/5), y=int(self.height/50))
            if type(self).__name__ != "HomeScreen" :
                home_button = Button(self.frame, width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)), text="Home", command=lambda: self.changeScreen("Home")).place(x=int(self.width - self.width/2.5), y=int(self.height/50))
        
        self.canvas.pack()

    def changeScreen(self, screen:str, user:int=0):
        if not self.screens.get(screen) :
            raise KeyError("This screen does not exist.")
        self.canvas.destroy()
        self.frame.destroy()
        if screen == "Home":
            self = self.screens[screen](self.root, self.screens, self.database, user)
        else :
            self = self.screens[screen](self.root, self.screens, self.database)

    def logout(self) :
        self.current_user = ""
        self.changeScreen("Login")
