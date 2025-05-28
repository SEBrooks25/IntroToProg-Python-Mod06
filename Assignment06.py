# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions, classes, &
# the separations of concerns pattern.
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sophia Brooks, 05/28/25, Edited Script
# ------------------------------------------------------------------------------------------ #
import json

# -- Data Constants -- #
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# -- Processing Classes -- #
class FileProcessor:
    """
    Handles reading and writing student data to a file.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, "r") as file:
                student_data.extend(json.load(file))
        except FileNotFoundError as e:
            IO.output_error_messages("File not found.", e)
        except Exception as e:
            IO.output_error_messages("General error reading file.", e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            print("The following data was saved to file!")
            IO.output_student_courses(student_data)
        except Exception as e:
            IO.output_error_messages("Error saving to file.", e)


# -- Presentation (Input/Output) Classes -- #
class IO:
    """
    Handles input and output from the user.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(f"Error: {message}")
        if error:
            print("-- Technical Error Message --")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        print(menu)

    @staticmethod
    def input_menu_choice():
        return input("What would you like to do: ")

    @staticmethod
    def output_student_courses(student_data: list):
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": first_name, "LastName": last_name, "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {first_name} {last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(str(e), e)
        except Exception as e:
            IO.output_error_messages("General input error.", e)
        return student_data


# -- Main Body -- #
students: list = []
students = FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(students)
    elif menu_choice == "2":
        IO.output_student_courses(students)
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")