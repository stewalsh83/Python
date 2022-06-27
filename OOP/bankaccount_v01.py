class Bankaccount(object):

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficiant funds avilable")

    def __str__(self):
        return "Your current balance is: {:.2f} euro".format(self.balance)


b = Bankaccount(100)
print(b.balance)

b.withdraw(50)
print(b.balance)

b.withdraw(100)

print(b.balance)

b.balance -= 100
print(b.balance)

b.balance -= 1000000
print(b.balance)
