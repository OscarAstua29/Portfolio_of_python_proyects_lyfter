def my_decorator(func):
    def wrapper(a,b):
        for i in [a,b]:
            type_of_variable=(type(i)) 
            if type_of_variable != int:
                raise ValueError("PARAMETER {i} IS NOT A NUMBER")
            else:
                print("PARAMETER {i} IS A NUMBER")
        return func (a,b)             
    return wrapper

@my_decorator
def numbers(a, b):

    return  a+b

numbers(3, 'a')
