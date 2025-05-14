class Bank:
    bank = "UBL"

    def __init__(self, customer):
        self.customer = customer
        print(f"{self.customer} is a customer of {self.bank}")

    @classmethod
    def ChangeBank(cls, new_bank):
        cls.bank = new_bank

customer1 = Bank("Ali")
customer2 = Bank("Sara")

customer1.ChangeBank("HBL")

customer1 = Bank("Ali")
customer2 = Bank("Sara")