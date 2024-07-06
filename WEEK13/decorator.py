def my_decorator(func):
    def wrapper(a,b):
        result = func(a, b)
        print(f'RESULT = {result}')
        return result
    return wrapper

@my_decorator
def parameters(a, b):
    return a + b

parameters(3, 4)