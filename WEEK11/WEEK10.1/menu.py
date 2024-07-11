from actions import StudentInfo
from actions import Student

def display_menu():
    student_info = StudentInfo()
    while True:
        Student.clear_screen()
        print("MENU")
        print("1. Add Student to Register")
        print("2. Print Student Register")
        print("3. Get Best 3 Averages")
        print("4. Get Grade Average Between All Students")
        print("5. Export Student Register to CSV")
        print("6. Import Student Register from CSV")
        print("7. Exit")
        try:
            option_selected = int(input("Select an option: "))
            if option_selected == 7:
                break
            elif option_selected == 1:
                student_info.add_to_register()
            elif option_selected == 2:
                student_info.print_student_register()
            elif option_selected == 3:
                student_info.get_best_3_average()
            elif option_selected == 4:
                student_info.get_grade_average_between_all_students()
            elif option_selected == 5:
                student_info.export_student_register_on_a_csv()
            elif option_selected == 6:
                student_info.import_student_register()
            else:
                print('INVALID INPUT, PLEASE ENTER A VALID VALUE')
                input('PRESS ENTER TO CONTINUE\n')
        except ValueError:
            print('INVALID INPUT, PLEASE ENTER A NUMBER')
            input('PRESS ENTER TO CONTINUE\n')
