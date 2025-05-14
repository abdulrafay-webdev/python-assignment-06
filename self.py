class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:",self.name)
        print("Age:",self.age) 


student1 = student("John", 20)
student2 = student("alex", 22)

student1.show()
student2.show()
