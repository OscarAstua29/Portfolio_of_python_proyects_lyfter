import menu


def run_program ():
    student_register =[]
    while True:
        try:
            new_student_register = menu.get_menu_value(student_register)
            if new_student_register is not None: 
                student_register = new_student_register
        except Exception as error:
            print(error)
            input('PRESS ENTER TO CONTINUE')

run_program()