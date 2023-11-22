# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   GNuesca,11/22/2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
menu_choice: str = ''
students: list = []  # a table of student data

class FileProcessor:
    '''
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    GNuesca,11.22.2023,Created Class
    '''

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        ''' This function writes all collected data from students to file in JSON format

        ChangeLog: (Who, When, What)
        GNuesca,11.22.2023,Created function

        :return: student_data
        '''
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages('Text file must exist before running this script!', e)
        except Exception as e:
            IO.output_error_messages('There was a non-specific error!', e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        ''' This function writes all collected data from students to file in JSON format

        ChangeLog: (Who, When, What)
        GNuesca,11.22.2023,Created function

        :return: none
        '''
        try:
            file = open(file_name, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
                IO.output_error_messages('Please check that the data is a valid JSON format', e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

class IO:
    '''
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    GNuesca,11.22.2023,Created Class
    '''
    pass
    @staticmethod
    def output_menu(menu: str):
        ''' This function displays menu choices to the user

        ChangeLog: (Who, When, What)
        GNuesca,11.22.2023,Created function

        :return: None
        '''
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        ''' This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        GNuesca,11.22.2023,Created function

        :return: string with the users choice
        '''
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        ''' This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        GNuesca,11.22.2023,Created function

        :return: student_data
        '''
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages('That value is not the correct type of data!', e)
        except Exception as e:
            IO.output_error_messages('There was a non-specific error!', e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: dict):
        ''' This function displays the first names, last names, and course names collected

        ChangeLog: (Who, When, What)
        GNuesca,11.22.2023,Created function

        :return: none
        '''
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        GNuesca,11.22.2023,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

#  End of function definitions


# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")