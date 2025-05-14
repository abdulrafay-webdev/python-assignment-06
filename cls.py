class counter:
    count = 0
    def __init__(self):
        counter.count +=1

    def display(cls):
        print("Total Count:",cls.count)

counter1 = counter()
counter2 = counter()
counter3 = counter()
counter4 = counter()
counter5 = counter()

counter1.display()