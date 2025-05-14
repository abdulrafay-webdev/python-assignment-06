class Person:
    def __init__(self,name):
        self.name = name
        print(f"Person {self.name} created")

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
        print("Teacher created")

T = Teacher("Ali","Math")
print(f"Teacher {T.name} teaches {T.subject}")                