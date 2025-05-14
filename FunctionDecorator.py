def log_function(func):
    def wrapper():
        print("function is being called")
        func()
    return wrapper

@log_function
def say_hello():
    print("Hello!")

say_hello()    