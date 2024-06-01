class StudentName:
    def __init__(self):
        self.student_name = input("ENTER THE STUDENT NAME: ")

class StudentGrade:
    def __init__(self):
        self.student_grade = input("ENTER THE STUDENT GRADE: ")

class StudentSchool:
    def __init__(self):
        self.student_school = input("ENTER THE STUDENT SCHOOL: ")

class RegisterScientificFeria(StudentGrade, StudentSchool, StudentName):
    def __init__(self):
        StudentName.__init__(self)
        StudentGrade.__init__(self)
        StudentSchool.__init__(self)


new_student = RegisterScientificFeria()
print('STUDENT NAME:', new_student.student_name)
print('STUDENT GRADE:',new_student.student_grade)
print('STUDENT SCHOOL:',new_student.student_school)