# import time
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function
# def delay_decorator2(function):
#     def wrapper_function():
#         function()
#         function()
#     return wrapper_function
# @delay_decorator
# def hello():
#     print("Hello")
    
# @delay_decorator2   
# def bye():
#     print("Bye")
    
# #main()
# hello()
# bye()
import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        time.sleep(1)
        function()
    return wrapper_function

def fast_function():
    for i in range(10000000):
        i * i
@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i
        
fast_function()
end_time = time.time()
print(end_time-current_time)
slow_function()
end_time = time.time()
print(end_time-current_time)
    