from tkinter import *

top_bar_color = "Red"
logo_background = "White"
button_background = "Blue"

class Screen:
    def __init__(self, root:Tk, frame:Frame, screens:dict):
        self.root = root
        self.frame = frame
        self.screens = screens

        self.root.title("Blank Screen")
        
        self.root.update()
        self.height = self.root.winfo_height()
        self.width = self.root.winfo_width()
        self.canvas = Canvas(frame, width=self.width, height=self.height)
        
        self.canvas.create_rectangle(0, 0, self.width, (self.height/10), fill=top_bar_color)
        self.canvas.create_rectangle((self.width/50), (self.height/50), (self.width/5), (self.height/10 - self.height/50), fill=logo_background) # Logo
        if type(self).__name__ != "LoginScreen" :
            logout_button = Button(self.frame, width=int(((self.width/50)-(self.width/500))*1.5), height=int((self.height/100)-(self.height/160)), text="Log out", command=lambda: self.changeScreen("Login")).place(x=int(self.width - self.width/5), y=int(self.height/50))

        self.canvas.pack()

    def changeScreen(self, screen):
        if not self.screens.get(screen) :
            raise KeyError("This screen does not exist.")
        self.canvas.destroy()
        self = self.screens[screen](self.root, self.frame, self.screens)