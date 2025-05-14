def add_greeting(cls):
    def greet(self):
        print("Hello From Decorator!")
    cls.greet = greet
    return cls


@add_greeting
class Person:
    def __init__(self,name):
        self.name = name

p = Person("John")
print(p.greet())
