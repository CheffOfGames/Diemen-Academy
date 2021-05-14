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
x_pos, y_pos = int(width / 24), int(height / 8)
root.resizable(0,0)
root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")

# UI shit
ui_height, ui_width, ui_x_pos, ui_y_pos = int(width / 8), int(width / 4), int(x_pos*1.5 + width), (y_pos)
ui_root = Tk()
ui_root.resizable(0,0)
ui_root.geometry(f"{ui_width}x{ui_height}+{ui_x_pos}+{ui_y_pos}")

# Set frames + canvas
frame = Frame(root, width=width, height=height, bg=background_color)
frame.pack()
ui_frame = Frame(root, width=ui_width, height=ui_height)
frame.pack()

# Current page
current_page = EnrollScreen(root, frame, screens)

# # Change page
# screens_list = []
# for i in range(len(screens)) :
#     screens_list += str(i)

# var = StringVar(ui_root)
# var.set(screens_list[0])

# screens_menu = OptionMenu(ui_frame, var, *screens_list)
# screens_menu.config(width=int(ui_width/2))
# screens_menu.pack(side="top")

# def callback(*args) :
#     current_page.changeScreen(var.get())

# var.trace("w", callback)

# End of file
root.mainloop()
ui_root.mainloop()