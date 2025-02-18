class Student:
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year Level: {self.year_level}")
        print("------------------------------------------------------")
    print("        \t\t  STUDENTS INFORMATION         ")
    print("------------------------------------------------------")

# Instantiation of three Students
s1 = Student("2023201716", "Andrea M. Valdez", "BS CpE", "2")
s2 = Student("2023202500", "Elaiza Czarina Claire C. Bautista", "BS CpE", "2")
s3 = Student("2023203553", "Austine Arvie E. Torres", "BS CpE", "2")

# Display the information
s1.display_info()
s2.display_info()
s3.display_info()