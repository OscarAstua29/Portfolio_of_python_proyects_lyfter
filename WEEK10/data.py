import csv
import os

def clear_screen_data_file():
    os.system('cls' if os.name == 'nt' else 'clear')


def export_student_in_register(student_register):
        
    with open('WEEK10/student_register.csv', 'w', newline='') as file_w:
        fieldnames = ['name', 'second name','complete name','class', 'spanish grade', 'english grade', 'social studies grade', 'science grade', 'total average']
        writer = csv.DictWriter(file_w, fieldnames=fieldnames)

        if file_w.tell() == 0:
            writer.writeheader()
        for student in student_register:
            writer.writerow({
                'name': student['student']['name'],
                'second name': student['student']['second name'],
                'complete name': student['student']['complete name'],
                'class': student['student']['class'],
                'spanish grade': student['grades']['spanish grade'],
                'english grade': student['grades']['english grade'],
                'social studies grade': student['grades']['social studies grade'],
                'science grade': student['grades']['science grade'],
                'total average': student['grades']['total average']
            })
        
        print('--- STUDENT REGISTER EXPORTED SUCCESSFULLY ---')
        input ('----- PRESS ENTER TO CONTINUE -----\n')


def import_student_register():

    student_register=[]

    while True:
        file_path = input('PLEASE, ENTER DE FILE PATH TO IMPORT THE INFORMATION: \n') 
        with open(file_path, 'r', newline='') as file_r:
            file_imported = csv.DictReader(file_r)
            for student_data in file_imported:
                student_info = {
                    'name' : student_data['name'],
                    'second name' : student_data['second name'],
                    'complete name' :student_data['complete name'],
                    'class': student_data['class'],
                }
                grades_info = {
                    'spanish grade': student_data['spanish grade'],
                    'english grade': student_data['english grade'],
                    'social studies grade': student_data['social studies grade'],
                    'science grade': student_data['science grade'],
                    'total average': student_data['total average']
                }
                student_data['student'] = student_info
                student_data['grades'] = grades_info      
                del student_data['name']
                del student_data['second name']
                del student_data['complete name']
                del student_data['class']
                del student_data['spanish grade']
                del student_data['english grade']
                del student_data['social studies grade']
                del student_data['science grade']
                del student_data['total average']
                student_register.append(student_data)
        break
    print("--- STUDENT REGISTER IMPORTED SUCCESSFULLY ---")
    input ("----- PRESS ENTER TO CONTINUE -----")
    return student_register
















def find_students_average ():
    student_register = "Semana 9/student_register.csv"
    if os.path.getsize(student_register) > 0:
        with open("Semana 9/student_register.csv", "r", ) as file_r:
            reader = csv.DictReader(file_r)
            list_of_register_complete = []
            for row in reader:
                list_of_register_complete.append(row)
    else:
        print("NO DATA YET")

    return list_of_register_complete



