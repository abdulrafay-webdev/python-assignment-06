class Employee:
    def __init__(self,name,role):
        self.name = name
        self.role = role
        
    def details(self):
        print(f"{self.name} is a {self.role}")

class Department:
    def __init__(self,name,employee):
        self.name = name
        self.employee = employee

    def department_details(self):
        print(f"Department: {self.name}")
        employee_detail = self.employee.details()
        print(f"{employee_detail}")

amp1 = Employee("John Doe","Software Engineer")
dept1 = Department("IT",amp1)
dept1.department_details()        