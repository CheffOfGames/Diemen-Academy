from tkinter import *
from enrollScreen import *
from gradesScreen import *
from homeScreen import *
from loginScreen import *
from profileScreen import *
from scheduleScreen import *
from subjectScreen import *

# Define variables
screens = {"Enroll": EnrollScreen, "Grades": GradesScreen, "Home": HomeScreen, "Login": LoginScreen, "Profile": ProfileScreen, "Schedule": ScheduleScreen, "Subject": SubjectScreen}
database = ""

# Start windows
root = Tk()
height, width = int(root.winfo_screenheight() * 0.75), int(root.winfo_screenwidth() * 0.75)
x_pos, y_pos = int(width / 24), int(height / 8)
root.resizable(0,0)
root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")

# Current page
current_page = LoginScreen(root, screens, database)

# Change page
screens_list = ["Home", "Enroll", "Grades", "Login", "Profile", "Schedule", "Subject"]

# End of file
root.mainloop()