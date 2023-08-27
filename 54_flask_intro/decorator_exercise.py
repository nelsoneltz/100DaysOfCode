import time
current_time = time.time()
# print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
        # function.__name__ returns the name of the function used
    return wrapper_function

# Decorator structure
# Decorator is function, with a wrapper function inside;
# Add steps to the wrapper function, add the function within the wrapper
# return the wrapper function at the end

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
        
fast_function()
slow_function()