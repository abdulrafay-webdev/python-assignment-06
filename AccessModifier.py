class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

    def ssn_display(self):
        return self.__ssn

emp = Employee("Ali", 50000, "123-45-6789")

# ✅ Public - Accessible
print("Name:", emp.name)

# ⚠️ Protected - Accessible but not recommended
print("Salary:", emp._salary)

# ❌ Private - Direct access not allowed
try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Private access error:", e)


# ✅ Accessing private via using a method
ssn_employee = emp.ssn_display()
print("SSN (using method):", ssn_employee)


# ✅ Accessing private via name mangling
print("Private SSN (using name mangling):", emp._Employee__ssn)
