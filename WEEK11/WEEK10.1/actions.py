import os
from collections import defaultdict
from data import export_student_in_register, import_student_register

class Student:
    def __init__(self, name, second_name, student_class, spanish_grade, english_grade, social_studies_grade, science_grade):
        self.name = name.upper()
        self.second_name = second_name.upper()
        self.student_class = student_class.upper()
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade
        self.complete_name = f"{self.name} {self.second_name}"
        self.total_average = (self.spanish_grade + self.english_grade + self.social_studies_grade + self.science_grade) / 4

    @classmethod
    def get_all_student_values(cls):
        student_name = cls.get_student_values_string('STUDENT NAME').upper()
        student_second_name = cls.get_student_values_string('STUDENT SECOND NAME').upper()
        student_class = cls.get_student_values_string('STUDENT CLASS').upper()
        student_spanish_grade = cls.get_student_values_int('SPANISH')
        student_english_grade = cls.get_student_values_int('ENGLISH')
        student_social_studies_grade = cls.get_student_values_int('SOCIAL STUDIES')
        student_science_grade = cls.get_student_values_int('SCIENCE')
        return cls(student_name, student_second_name, student_class, student_spanish_grade, student_english_grade, student_social_studies_grade, student_science_grade)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_student_values_string(type_data_for_consult_in_string_function):
        while True:
            Student.clear_screen()
            try:
                student_data_obtained_string = input(f'ENTER THE {type_data_for_consult_in_string_function} FOR THE REGISTRATION: ')
                break
            except ValueError:
                Student.clear_screen()
                print('INVALID INPUT, PLEASE ENTER A VALID VALUE')
                input('PRESS ENTER TO CONTINUE')
        return student_data_obtained_string

    @staticmethod
    def get_student_values_int(type_data_for_consult_in_int_function):
        while True:
            Student.clear_screen()
            try:
                while True:
                    student_data_obtained_int = int(input(f'ENTER THE {type_data_for_consult_in_int_function} GRADE FOR THE REGISTRATION: '))
                    if 0 <= student_data_obtained_int <= 100:
                        break
                    else:
                        Student.clear_screen()
                        print('INVALID INPUT, PLEASE ENTER A VALID VALUE BETWEEN 0 TO 100')
                break
            except ValueError:
                Student.clear_screen()
                print('INVALID INPUT, PLEASE ENTER A VALID VALUE')
                input('PRESS ENTER TO CONTINUE')
        return student_data_obtained_int

class StudentInfo:
    def __init__(self):
        self.students_register = []

    def add_to_register(self):
        create_student = Student.get_all_student_values()
        self.students_register.append(create_student)
        print('STUDENT ADDED TO THE REGISTER')
        input('PRESS ENTER TO CONTINUE')

    def print_student_register(self):
        if not self.students_register:
            print('STUDENT REGISTER EMPTY')
        else:
            for i, student in enumerate(self.students_register):
                print(f'-----STUDENT {i+1}-----')
                print(f'COMPLETE NAME: {student.complete_name}')
                print(f'CLASS: {student.student_class}')
                print(f'TOTAL AVERAGE: {student.total_average}')
                print(f'SPANISH GRADE: {student.spanish_grade}')
                print(f'ENGLISH GRADE: {student.english_grade}')
                print(f'SOCIAL STUDIES GRADE: {student.social_studies_grade}')
                print(f'SCIENCE GRADE: {student.science_grade}')
            print('PRINTING COMPLETE')
        input('PRESS ENTER TO CONTINUE')

    def get_best_3_average(self):
        average_groups = defaultdict(list)
        for student in self.students_register:
            average_groups[student.total_average].append(student)
        sorted_averages = sorted(average_groups.keys(), reverse=True)
        current_rank = 1
        for average in sorted_averages:
            students = average_groups[average]
            if current_rank <= 3:
                for student in students:
                    print(f'TOP {current_rank} AVERAGE')
                    print(f'{student.complete_name}')
                    print(f'AVERAGE: {student.total_average}%\n')
                current_rank += 1
            else:
                break
        if current_rank == 1:
            print('STUDENT LIST EMPTY')
        elif current_rank == 2:
            print('NOT TOP 2 STUDENT AVERAGE')
        elif current_rank == 3:
            print('NOT TOP 3 STUDENT AVERAGE')
        input("PRESS ENTER TO CONTINUE")
        

    def get_grade_average_between_all_students(self):
        total_averages = defaultdict(list)
        number_of_student_checked = 0
        sum_of_averages = 0
        if not self.students_register:
            input('STUDENT LIST EMPTY')
            return
        for student in self.students_register:
            total_averages[student.total_average].append(student.total_average)
            sum_of_averages += student.total_average
            number_of_student_checked += 1
        if number_of_student_checked == 0:
            print('NO STUDENTS TO CALCULATE AVERAGE')
        else:
            global_average = sum_of_averages / number_of_student_checked
            print(f'THE GLOBAL AVERAGE IS: {global_average}\n')
        input("PRESS ENTER TO CONTINUE")

    def export_student_register_on_a_csv(self,):
        export_student_in_register(self.students_register)

    def import_student_register(self,):
        self.students_register = import_student_register(Student)
