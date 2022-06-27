class Bankaccount(object):

    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
        else:
            print("Insufficiant funds avilable")

    def __str__(self):
        return "Your current balance is: {:.2f} euro".format(self._balance)


def _bonus(self):
    self._balance += 1000000

# private attributes are marked with an underscore
# methods are also attributes
