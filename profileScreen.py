from tkinter import *
from blankScreen import *

class ProfileScreen(Screen):
    def __init__(self, root: Tk, screens: dict, database, user="", usertype:int=-1):
        # Set variables
        super().__init__(root, screens, database, user=user, usertype=usertype)
        self.root.title("Profile Screen")

        # Check if user is Student
        if self.current_usertype == 0:
            # Gather data from student to be shown
            self.cursor.execute(f"  select a.first_name, a.last_name, a.date_of_birth, a.nationality, a.gender, a.email, a.start_year, b.study_name, a.studycounselor, c.street, c.house_number, c.postal_code, c.city, c.phone\
                                    from student a, study b, adress c\
                                    where b.id=a.fk_study_id\
                                    and c.id=a.fk_adress_id\
                                    and a.id={self.current_user}; ")
            profile_info = self.cursor.fetchall()[0]

            # Print userdata
            self.personalinfo = Label(self.root, text=f"Name: {profile_info[0]} {profile_info[1]} \nBorn: {profile_info[2]}\
                            \nNationality: {profile_info[3]} \nGender: {profile_info[4]}", justify='left').place(x =(self.width/4) , y= (self.height/7))
            # Check if email has been entered before printing
            if profile_info[5] == '  ':
                self.schoolinfo = Label(self.root, text=f"Start Year: {profile_info[6]}\nStudy: {profile_info[7]}\nStudy Counselor: {profile_info[8]}", justify='left').place(x =(self.width/4) , y= (3*self.height/7))                  
            else:
                self.schoolinfo = Label(self.root, text=f"Email: {profile_info[5]} \nStart Year: {profile_info[6]}\nStudy: {profile_info[7]}\nStudy Counselor: {profile_info[8]}", justify='left').place(x =(self.width/4) , y= (3*self.height/7))                  

            # Print contact information
            self.contactinfo = Label(self.root, text=f"{profile_info[9]} {profile_info[10]} \n{profile_info[11]} \n{profile_info[12]} \n{profile_info[13]}", justify='left').place(x =(self.width/4) , y= (5*self.height/7))            

            # Add rectangle in place for picture
            self.canvas.create_rectangle((self.width/15), (self.height/7), (self.width/6), (self.height/2.5))
        
        # Check if user is Teacher
        elif self.current_usertype == 1:
            # Gather data from teacher to be shown
            self.cursor.execute(f"select a.first_name , a.last_name , a.date_of_birth, a.nationality, a.gender, a.salary, a.study_counselor, c.street, c.house_number, c.postal_code, c.city, c.phone from teacher a, adress c\
                                    where a.fk_adress_id = c.id\
                                    and a.id ={self.current_user}")
            profile_info = self.cursor.fetchall()[0]
            
            # Print and place userdata
            self.personalinfo = Label(self.root, text=f"Name: {profile_info[0]} {profile_info[1]} \nBorn: {profile_info[2]}\
                            \nNationality: {profile_info[3]} \nGender: {profile_info[4]} \nSalary: {profile_info[5]} \nStudent Counselor (Y/N): {profile_info[6]} ", justify='left').place(x =(self.width/4) , y= (self.height/7))

            # Print and place contact information
            self.contactinfo = Label(self.root, text=f"{profile_info[7]} {profile_info[8]} \n{profile_info[9]} \n{profile_info[10]} \n{profile_info[11]}", justify='left').place(x =(self.width/4) , y= (5*self.height/7))
