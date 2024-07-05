import os
from actions import initialize_option_selected_in_menu

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_menu_value (student_register):
    while True:
        try: 
            clear_screen()
            print('---- {STUDENT CONTROL SYSTEM} ----\n')
            print('------------- {MENU} -------------\n')
            print('--{ENTER THE OPTION YOU PREFER}--\n')
            print(' PRESS (1) TO REGISTER A STUDENT\n PRESS (2) TO SEE STUDENTS REGISTER LIST\n PRESS (3) TO SEE TOP THREE STUDENTS WITH THE BEST TOTAL AVERAGE \n PRESS (4) TO SEE TOTAL AVERAGE PER STUDENT \n PRESS (5) TO EXPORT THE DATA OF STUDENTS REGISTER TO A CSV FILE  \n PRESS (6) TO IMPORT A CSV FILE \n PRESS (7) TO CHANGE A STUDENT GRADE \n')
            menu_value = int(input('ENTER AN OPTION: '))
            clear_screen()
            break
        except ValueError:
            clear_screen()
            print ('INVALID INPUT, PLEASE ENTER A VALID VALUE')
        input('PRESS ENTER TO CONTINUE \n')
    student_register = initialize_option_selected_in_menu(menu_value, student_register)
    return student_register
