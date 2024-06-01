import os
import data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_to_register(student_register):
    student_register.append(get_all_student_values())
    print('STUDENT ADDED TO DE REGISTER')
    input('PRESS ENTER TO CONTINUE')
    return student_register


def get_student_values_string (type_data__for_consult_in_string_function):

    while True:
        clear_screen()
        try:
            student_data_obtained_string = input(f'ENTER THE {type_data__for_consult_in_string_function} FOR THE REGISTRATION : ')
            break
        except ValueError:
            clear_screen()
            print ('INVALID INPUT, PLEASE ENTER A VALID VALUE')
            input ('PRESS ENTER TO CONTINUE')
    return student_data_obtained_string


def get_student_values_int (type_data__for_consult_in_int_function):

    while True:
        clear_screen()
        try:
            while True:
                student_data_obtained_int = int(input(f'ENTER THE {type_data__for_consult_in_int_function} GRADE FOR THE REGISTRATION: '))
                if student_data_obtained_int <= 100 and student_data_obtained_int >= 0:
                    break
                else:
                    clear_screen()
                    print ('INVALID INPUT, PLEASE ENTER A VALID VALUE BETWEEN 0 TO 100')
            break
        except ValueError:
            clear_screen()
            print ('INVALID INPUT, PLEASE ENTER A VALID VALUE')
            input ('PRESS ENTER TO CONTINUE')
    return student_data_obtained_int


def get_all_student_values ():

    student_name = get_student_values_string('STUDENT NAME').upper()
    student_second_name = get_student_values_string('STUDENT SECOND NAME').upper()
    student_class = get_student_values_string('STUDENT CLASS').upper()
    student_spanish_grade = get_student_values_int('SPANISH')
    student_english_grade = get_student_values_int('ENGLISH')
    student_social_studies_grade = get_student_values_int('SOCIAL STUDIES')
    student_science_grade = get_student_values_int('SCIENCE')
    student_complete_name = (student_name + ' ' + student_second_name)
    student_total_average = (student_spanish_grade + student_english_grade + student_social_studies_grade + student_science_grade)/4
    return  {
        'student' : {
        'name' : student_name,
        'second name' : student_second_name,
        'complete name' : student_complete_name,
        'class' : student_class
    },
    'grades': {
        'spanish grade': student_spanish_grade,
        'english grade': student_english_grade,
        'social studies grade': student_social_studies_grade,
        'science grade': student_science_grade,
        'total average': student_total_average,
    }
    }


def print_student_register(student_register):
    if student_register == []:
        print('STUDENT REGISTER EMPTY')
    else:
        for i in range(len(student_register)):
            print (f'-----STUDENT {i+1}-----')
            print(f'COMPLETE NAME: {student_register [i] ["student"] ["complete name"]}  \n')
            print(f'CLASS: {student_register [i] ["student"] ["class"]}  \n')
            print(f'TOTAL AVERAGE: {student_register [i] ["grades"] ["total average"]}  \n')
            print(f'SPANISH GRADE: {student_register [i] ["grades"] ["spanish grade"]}  \n')
            print(f'ENGLISH GRADE: {student_register [i] ["grades"] ["english grade"]}  \n')
            print(f'SOCIAL STUDIES GRADE: {student_register [i] ["grades"] ["social studies grade"]}  \n')
            print(f'SCIENCE GRADE: {student_register [i] ["grades"] ["science grade"]}  \n')
        print('PRINTING COMPLETE')
    input('PRESS ENTER TO CONTINUE\n')


def get_best_3_average(student_register):
    
    first_average = []
    second_average = []
    third_average = []

    if student_register == []:
        print('STUDENT REGISTER EMPTY')
    else:
        for row in student_register: 
                owner_average = row['student']['complete name']
                evaluate_average = row['grades']['total average']
                if not first_average:
                    first_average = {'student': owner_average, 'total average': evaluate_average}
                elif first_average['total average'] < evaluate_average:
                    third_average = second_average
                    second_average = first_average
                    first_average = {'student': owner_average, 'total average': evaluate_average}
                elif first_average['total average'] == evaluate_average:
                    first_average['student'] += f" AND {owner_average}"
                elif not second_average:
                    second_average = {'student': owner_average, 'total average': evaluate_average}
                elif second_average['total average'] < evaluate_average:
                    third_average = second_average
                    second_average = {'student': owner_average, 'total average': evaluate_average}
                elif second_average['total average'] == evaluate_average:
                    second_average['student'] += f" AND {owner_average}"
                elif not third_average:
                    third_average = {'student': owner_average, 'total average': evaluate_average}
                elif third_average['total average'] < evaluate_average:
                    third_average = {'student': owner_average, 'total average': evaluate_average}
                elif third_average['total average'] == evaluate_average:
                    third_average['student'] += f" AND {owner_average}"
        print(f'TOP 1 AVERAGE')
        print(f'{first_average["student"]}')
        print(f'AVERAGE: {first_average["total average"]}%\n')
        print(f'TOP 2 AVERAGE')
        if not second_average :
            print('NO DATA\n')
        else:
            print(f'{second_average["student"]}')
            print(f'AVERAGE:{second_average["total average"]}%\n')
        print(f'TOP 3 AVERAGE')
        if not third_average:
            print('NO DATA\n')
        else:
            print(f'{third_average['student']}')
            print(f'AVERAGE:{third_average["total average"]}%\n')
    input('PRESS ENTER TO CONTINUE')


def get_grade_average_between_all_students(student_register):

    number_of_student_checked = 0 
    sum_of_averages = 0

    if not student_register :
        print('STUDENT REGISTER EMPTY')
    else:
        for student_registered in student_register:
            number_of_student_checked += 1
            sum_of_averages += student_registered['grades']['total average']
        global_average = sum_of_averages/number_of_student_checked
        print(f' THE GLOBAL AVERAGE IS: {global_average}\n')
    input("PRESS ENTER TO CONTINUE")


def export_student_register_on_a_csv (student_register):
    if not student_register:
        print('STUDENT REGISTER EMPTY ')
        input('PRESS ENTER TO CONTINUE')
    else:
        data.export_student_in_register(student_register)


def import_student_register (student_register):

    while True:
        try:
                student_register= data.import_student_register()
                break
        except Exception as ex:
            print(ex)
            input('WE CAN NOT FIND DE FILE, PLEASE VERIFY THAT THE FILE EXIST.\n PRESS ENTER TO BACK TO MENU\n')
            break
    return student_register


def get_new_value_to_change_in_register_for_int(student_register, student_number_selected, subject):

    while True:
        try:
            student_data_obtained_int = int(input(f'ENTER THE NEW {subject.upper()}: '))
            if 0 <= student_data_obtained_int <= 100:
                student_register[student_number_selected]['grades'][subject] = str(student_data_obtained_int)
                total_sum = sum(int(value) for key, value in student_register[student_number_selected]['grades'].items() if key != 'total average')
                total_average = total_sum / (len(student_register[student_number_selected]['grades']) - 1)
                student_register[student_number_selected]['grades']['total average'] = str(total_average)
                break
            else:
                print('INVALID INPUT, PLEASE ENTER A VALUE BETWEEN 0 AND 100')
        except ValueError:
            print('INVALID INPUT, PLEASE ENTER A VALID INTEGER VALUE')
            input ('PRESS ENTER TO CONTINUE')
    return student_register


def change_a_value_of_a_student(student_register):
    if not student_register:
        print('STUDENT REGISTER IS EMPTY')
    else:
        while True:
            try:
                student_number_selected = int(input('ENTER THE STUDENT NUMBER YOU WANT TO CHANGE: ')) - 1
                if 0 <= student_number_selected < len(student_register):
                    print(f'----STUDENT {student_number_selected + 1}-----')
                    print(f'COMPLETE NAME: {student_register[student_number_selected]["student"]["complete name"]}')
                    print(f'CLASS: {student_register[student_number_selected]["student"]["class"]}')
                    print(f'TOTAL AVERAGE: {student_register[student_number_selected]["grades"]["total average"]}')
                    print(f'SPANISH GRADE: {student_register[student_number_selected]["grades"]["spanish grade"]}')
                    print(f'ENGLISH GRADE: {student_register[student_number_selected]["grades"]["english grade"]}')
                    print(f'SOCIAL STUDIES GRADE: {student_register[student_number_selected]["grades"]["social studies grade"]}')
                    print(f'SCIENCE GRADE: {student_register[student_number_selected]["grades"]["science grade"]}')
                    print('--------------------------------------')
                    while True:
                        try:
                            value_to_change = input('ENTER THE OPTION YOU WANT TO CHANGE:\n PRESS 1 TO CHANGE THE NAME \n PRESS 2 TO CHANGE THE SECOND NAME\n PRESS 3 TO CHANGE THE CLASS\n PRESS 4 TO CHANGE THE SPANISH GRADE\n PRESS 5 TO CHANGE THE ENGLISH GRADE\n PRESS 6 TO CHANGE THE SOCIAL STUDIES GRADE\n PRESS 7 TO CHANGE THE SCIENCE GRADE\n OPTION : ')
                            if value_to_change == '1':
                                new_name = input('ENTER THE NEW NAME: ')
                                new_complete_name = new_name + ' ' + student_register[student_number_selected]['student']['second name']
                                student_register[student_number_selected]['student']['name'] = new_name.upper()
                                student_register[student_number_selected]['student']['complete name'] = new_complete_name.upper()
                            elif value_to_change == '2':
                                new_second_name = input('ENTER THE NEW SECOND NAME: ')
                                new_complete_name = student_register[student_number_selected]['student']['name'] + ' ' + new_second_name
                                student_register[student_number_selected]['student']['second name'] = new_second_name.upper()
                                student_register[student_number_selected]['student']['complete name'] = new_complete_name.upper()
                            elif value_to_change == '3':
                                new_class = input('ENTER THE NEW CLASS: ')
                                student_register[student_number_selected]['student']['class'] = new_class.upper
                            elif value_to_change in ['4', '5', '6', '7']:
                                subject_map = {'4': 'spanish grade', '5': 'english grade', '6': 'social studies grade', '7': 'science grade'}
                                subject = subject_map[value_to_change]
                                student_register = get_new_value_to_change_in_register_for_int(student_register, student_number_selected, subject)
                            break
                        except ValueError :
                            print('INVALID INPUT, PLEASE ENTER A VALID VALUE')
                            input('PRESS ENTER TO CONTINUE\n')
                    break
                else:
                    print('THE STUDENT NUMBER IS NOT IN THE LIST.')
                    input('PRESS ENTER TO CONTINUE\n')
            except ValueError:
                print('INVALID INPUT, PLEASE ENTER A VALID VALUE')
                input('PRESS ENTER TO CONTINUE\n')
    print('CHANGE WAS EXECUTING SUCCESSFULLY')
    return print(student_register)


def initialize_option_selected_in_menu (option_selected, student_register):

        menu_dict = {
        1 : add_to_register,
        2 : print_student_register,
        3 : get_best_3_average,
        4 : get_grade_average_between_all_students,
        5 : export_student_register_on_a_csv,
        6 : import_student_register,
        7 : change_a_value_of_a_student,
    }
        
        while True:
            start_option_selected = menu_dict[option_selected]
            if option_selected in menu_dict:
                student_register = start_option_selected(student_register)
                break
            else:
                print('INVALID INPUT, PLEASE ENTER A VALID VALUE')
            input('PRESS ENTER TO CONTINUE\n')
        return student_register