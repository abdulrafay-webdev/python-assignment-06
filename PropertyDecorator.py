class Product:
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value < 0:
            print("Price cannot be negative")
        self._price = value
        print(f"Price set to {self._price}")

    @price.deleter
    def price(self):
        del self._price
        print("Price deleted")


p = Product(100)
print(p.price)  # Accessing the price property
p.price = 150  # Setting the price property
print(p.price)  # Accessing the updated price property
del p.price  # Deleting the price property
p.price = 200  # Setting the price property again
print(p.price)  # Accessing the deleted price property        