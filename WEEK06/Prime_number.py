def prime_or_not(number,divisor, list_of_prime_numbers, list_of_not_prime_numbers):
    is_prime = True
    while divisor <= number // 2: 
        quotient = number % divisor 
        if quotient == 0:
            is_prime = False 
            break 
        divisor += 1
    save_on_lists(is_prime, number, list_of_prime_numbers, list_of_not_prime_numbers)
    

def save_on_lists (is_prime, number, list_of_prime_numbers, list_of_not_prime_numbers):

    

    if is_prime == True:
        list_of_prime_numbers.append(number)
    else:
        list_of_not_prime_numbers.append(number)
    return list_of_prime_numbers


def main ():
    list_of_prime_numbers = []
    list_of_not_prime_numbers = []
    list_of_numbers=[1, 4, 6, 7, 13, 9, 67]
    for index in list_of_numbers:
        prime_or_not(index,2, list_of_prime_numbers, list_of_not_prime_numbers)
    print(list_of_prime_numbers)