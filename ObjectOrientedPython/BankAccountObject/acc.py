class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as file:
            self.balance=int(file.read())
    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class creates a checking object"""
    type="checking"
    def __init__(self, filepath, fee):
        Account.__init__(self,filepath)
        self.fee=fee
    def transfer(self, amount):
        self.balance=self.balance-amount - self.fee
        
jack_checking = Checking("jack.txt", 1)
print(jack_checking.balance)
jack_checking.transfer(10)
jack_checking.commit()
print(jack_checking.balance)

john_checking = Checking("john.txt", 1)
print(john_checking.balance)
john_checking.transfer(10)
john_checking.commit()
print(john_checking.balance)

print(jack_checking.type)
print(jack_checking.__doc__)