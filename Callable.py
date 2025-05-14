class Multiplier:
    def __init__(self,factor):
        self.factor = factor

    def __call__(self,number):
        return number * self.factor

m = Multiplier(6)
print(callable(m))  # Check if m is callable
print(m(10))        