from tkinter import *
from enrollScreen import *
from gradesScreen import *
from homeScreen import *
from loginScreen import *
from profileScreen import *
from scheduleScreen import *
from subjectScreen import *
from AdminCourseScreen import *
from AdminGradesScreen import *
from AdminStudentScreen import *
from AdminTeacherScreen import *
from AdminExamScreen import *


# Define variables
screens = {"Enroll": EnrollScreen, "Grades": GradesScreen, "Home": HomeScreen, "Login": LoginScreen, "Profile": ProfileScreen, "Schedule": ScheduleScreen, "Subject": SubjectScreen, "AdminCourse":AdminCourseScreen, "AdminGrades":AdminGradesScreen, "AdminStudent":AdminStudentScreen, "AdminTeacher":AdminTeacherScreen,"AdminExam":AdminExamScreen}

# Set the starting screen
root = Tk()
height, width = int(root.winfo_screenheight() * 0.75), int(root.winfo_screenwidth() * 0.75)
x_pos, y_pos = int((root.winfo_screenwidth()-width)/2), int((root.winfo_screenheight()-height)/2)
root.resizable(0,0)
root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")

# Connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password!", #your own pw
  database="world" 
  )

# Current page
current_page = LoginScreen(root, screens, mydb)

# End of file
root.mainloop()