import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

def delay_decorator2(function):
    def wrapper_function():
        function()
        function()
    return wrapper_function

@delay_decorator
def hello():
    print("Hello")
    
@delay_decorator2   
def bye():
    print("Bye")
    
#main()
hello()
bye()
    