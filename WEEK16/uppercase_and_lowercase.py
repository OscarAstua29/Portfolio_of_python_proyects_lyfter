def sum_of_letter_case (my_string, num_of_upper_case = 0, num_of_lower_case= 0, space= 0):
    for char in my_string:

        if char.isupper():
            num_of_upper_case +=1
        elif char.islower():
            num_of_lower_case += 1

        else:
            space +=1

    print(f"There is a {num_of_upper_case} upper cases and {num_of_lower_case} lower cases")
    return num_of_upper_case, num_of_lower_case

print(sum_of_letter_case('Hola Mundo'))
