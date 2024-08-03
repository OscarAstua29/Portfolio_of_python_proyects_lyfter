def function_sum (list, total_sum=0):
    for value in list:
        total_sum = value + total_sum
    return total_sum



list = [4, 6, 2, 29]

print (function_sum(list))