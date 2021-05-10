from tkinter import *
from enrollScreen import *
from gradesScreen import *
from homeScreen import *
from loginScreen import *
from profileScreen import *
from scheduleScreen import *
from subjectScreen import *

# Define variables
background_color = "White"
screens = (EnrollScreen, GradesScreen, HomeScreen, LoginScreen, ProfileScreen, ScheduleScreen, SubjectScreen)

# Start windows
root = Tk()
height, width = int(root.winfo_screenheight() * 0.75), int(root.winfo_screenwidth() * 0.75)
x_pos, y_pos = int(width / 8), int(height / 8)
root.resizable(0,0)
root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")

# Set frames + canvas
frame = Frame(root, width=width, height=height, bg=background_color)
frame.pack()
canvas = Canvas(frame, width=width, height=height)

# Current page
current_page = Screen(root, frame, canvas, screens)

# End of file
canvas.pack()
root.mainloop()