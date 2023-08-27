# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args,**kwargs):
        print(f'Called {function.__name__}{args}')
        result = function(args[0],args[1],args[2])
        print(f"Returned: {result}")
    return wrapper



# Use the decorator 👇
@logging_decorator
def multiply_func(a,b,c):
    return a * b * c
multiply_func(1,2,3)