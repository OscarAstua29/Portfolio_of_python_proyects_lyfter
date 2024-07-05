import csv

def export_student_in_register(student_register):
    try:
        with open('DUAD/WEEK11/WEEK10.1/student_register.csv', 'w', newline='') as file_w:
            writer = csv.writer(file_w)
            writer.writerow(['Name', 'Second Name', 'Class', 'Spanish Grade', 'English Grade', 'Social Studies Grade', 'Science Grade'])
            for student in student_register:
                writer.writerow([
                    student.name,
                    student.second_name,
                    student.student_class,
                    student.spanish_grade,
                    student.english_grade,
                    student.social_studies_grade,
                    student.science_grade
                ])
        print(f'Student register exported.')
    except PermissionError:
        print(f'Permission denied: Unable to write. Please check your file permissions.')
    except FileNotFoundError:
        print(f'File not found: The directory does not exist.')
    except Exception as e:
        print(f'An error occurred: {e}')
    input('PRESS ENTER TO CONTINUE')

def import_student_register(Student):
    student_register = []
    file_path = input('PLEASE, ENTER THE NAME OF THE FILE TO IMPORT THE INFORMATION: \n')
    try:
        with open(f'DUAD/WEEK11/WEEK10.1/{file_path}', 'r', newline='') as file_r:
            reader = csv.DictReader(file_r)
            for row in reader:
                student = Student(
                    name=row['Name'],
                    second_name=row['Second Name'],
                    student_class=row['Class'],
                    spanish_grade=int(row['Spanish Grade']),
                    english_grade=int(row['English Grade']),
                    social_studies_grade=int(row['Social Studies Grade']),
                    science_grade=int(row['Science Grade'])
                )
                student_register.append(student)
        print(f'Student register imported from {file_path}.')
    except FileNotFoundError:
        print(f'File not found: The file {file_path} does not exist.')
    except PermissionError:
        print(f'Permission denied: Unable to read file {file_path}. Please check your file permissions.')
    except Exception as e:
        print(f'An error occurred: {e}')
    input('PRESS ENTER TO CONTINUE')
    return student_register



