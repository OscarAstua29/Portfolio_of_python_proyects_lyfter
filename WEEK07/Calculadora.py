import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds
    while time.time() < end_time:
        int(end_time - time.time())
        time.sleep(1)


def addition_function (number_a, number_b):
    return number_a + number_b


def subtraction_function(number_a, number_b):
    return number_a - number_b


def multiplication_function(number_a, number_b):
    return number_a * number_b


def divide_function(number_a, number_b):

    if number_b>= 1:
        result = number_a / number_b
        return result
    else: 
        print("You can not divide by 0")
        input ("Press enter to continue")
        user_consult()


def user_consult (b=0, number_c = 0, operator =""):
    try:
        
        if b==0 :
            clear_screen()
            number_a = int(input("Enter the first number: "))
            operator = input("Enter a option: \n (a) to addition \n (s) to subtraction \n (m) to multiplication \n (d) to divide \n (e) to exit: \n Option:")
            while operator != "a" and operator != "s" and operator != "m" and operator != "d" and operator != "e":
                     clear_screen()
                     print(f"Please, enter a valid input, press enter to continue." )
                     operator = input("Enter a option: \n (a) to addition \n (s) to subtraction \n (m) to multiplication \n (d) to divide \n (e) to exit: \n Option:")

            try: 
                if operator == "e":
                        exit()
                elif operator == "a" or operator == "s" or operator == "m" or operator == "d":
                        number_b = int(input("Enter the second number: "))
                        call_to_solve(operator, number_a, number_b)
            except ValueError as ex:
                 input(f"Please, enter a valid input, press enter to continue." )
                 user_consult(2,number_a, operator)

        elif b == 1 :
            operator = input("Enter a option: \n (a) to addition \n (s) to subtraction \n (m) to multiplication \n (d) to divide \n (e) to exit: \n Option:")
            while operator != "a" and operator != "s" and operator != "m" and operator != "d" and operator != "e":
                     clear_screen()
                     print (f"Last result: {number_c}")
                     print(f"Please, enter a valid input, press enter to continue." )
                     operator = input("Enter a option: \n (a) to addition \n (s) to subtraction \n (m) to multiplication \n (d) to divide \n (e) to exit: \n Option:")
            try: 
                if operator == "e":
                        exit()
                elif operator == "a" or operator == "s" or operator == "m" or operator == "d":
                        number_b = int(input("Enter the second number: "))
                        clear_screen()
                        call_to_solve(operator, number_c, number_b)
            except ValueError as ex:
                 input(f"Please, enter a valid input, press enter to continue." )
                 user_consult(2,number_c, operator)

        else:
             try:
                clear_screen()
                input(f"Please, enter a valid input, press enter to continue." )
                number_b = int(input("Enter the second number: "))
                clear_screen()
                call_to_solve(operator, number_c, number_b)
             except ValueError : 
                 input(f"Please, enter a valid input, press enter to continue." )
                 user_consult(2,number_c, operator)
             
    except ValueError as ex: 
        input(f"Please, enter a valid input, press enter to continue." )
        user_consult()


def call_to_solve (operator, number_a, number_b):

    operation_dict = {
    "a": addition_function,
    "s": subtraction_function,
    "d": divide_function,
    "m": multiplication_function,

}
    
    if operator in operation_dict:
            result = (operation_dict [operator] (number_a, number_b))
            print(f"Result: {result}")
            continue_the_equation_consult(result)
    else:
        print("Invalid character, please, entre a valid character.")
        timer(3)
        user_consult(1,number_a)


def continue_the_equation_consult (result = 0):
     try:
        continue_the_equation= input("Do you want to continue the equation? \n Press (y) to continue or press (n) to not continue: ")
        if continue_the_equation == "y" :
            user_consult(1,result)
        elif continue_the_equation == "n":
            final_equation = input("Do you want to exit? \n Press (n) to start a new equation, or press enter to exit : ")
            if final_equation == "n":
                user_consult()
            else:
                exit()
        else:
            clear_screen()
            print("Invalid input, enter a valid option")
            continue_the_equation_consult(result)
     except Exception as ex :
         clear_screen()
         print(ex)
         print("Invalid input, enter a valid option")
         continue_the_equation_consult(result)




def main ():
    operator = ""
    while operator != "e" :
        try: 
            user_consult()
        except Exception as ex:
            skip_the_error = input(f"An unexpected error occurred [{ex}] \n Restart? \n Press (r) to continue or press any other to exit." )
            if skip_the_error != "c":
                exit()
    exit()

main()