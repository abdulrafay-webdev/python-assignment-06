class Car:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")


Car1 = Car("Toyota")

print(Car1.brand)
Car1.start()

