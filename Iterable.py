class Countdown:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            print("number is less than or equal to 0")
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current        


cd = Countdown(100)

for num in cd:
    print(num)