from tkinter import *

top_bar_color = "Red"
logo_background = "White"
button_background = "Blue"

class Screen:
    def __init__(self, root:Tk, frame:Frame, screens:tuple):
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
        self.canvas.create_rectangle((self.width - self.width/5), (self.height/50), (self.width - self.width/50), (self.height/10-self.height/50), fill=button_background) # Logout button
        # https://stackoverflow.com/questions/11980812/how-do-you-create-a-button-on-a-tkinter-canvas

        self.canvas.pack()

    def changeScreen(self, screen):
        if screen not in self.screens :
            raise KeyError("This screen does not exist.")
        #self.canvas.delete("all")
        self.canvas = screen(self.root, self.frame, self.screens)