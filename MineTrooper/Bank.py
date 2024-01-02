class Bank:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def Deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return True
        else:
            print("Error: Expected value >= 0")
            return False

    def Withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        elif amount > self.balance:
            print("Error: Value greater than balance")
            return False
        else:
            print("Error: Expected value >= 0")
    
    def Reduce(self, amount):
        if amount >= self.balance:
            self.balance = 0
            return True
        elif 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Error: Expected value >= 0")
            return False

    def get_balance(self):
        return self.balance
    



