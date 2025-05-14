class InvalidAgeError(Exception):
    pass

def Check_age(age):
    if age < 18:
        raise InvalidAgeError("minimum age is 18")
    else:
        print("access granted")

try:
    user_age = int(input("enter your age: "))
    Check_age(user_age)
except InvalidAgeError as e:
    print("custom error caugth",e)    
