'''3.Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). 
Then, create two subclasses:

SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).'''


from abc import ABC
from typing import Any

class BankAccount (ABC):
    def __init__(self,balance = 0):
        self.balance = balance
    def deposit(self,amount):
        pass
    def withdraw (self,amount):
        pass
    def __get_balance(self):
        return self._balance 
    
class SavingAccount(BankAccount):
    def __init__(self, balance=500):
        super().__init__(balance)
    def deposit(self, amount):
        if amount > 0 :
            self._balance += amount 
        else:
            print("deposit amount must be positve")
    
    def withdraw(self, amount):
        if amount > 0 and self._balance-amount >=500:
            self._balance -=amount 
        else:
            print("insufficient funds minimum balance is ₹500.")

class CurrentAccount (BankAccount):
    def __init__(self, balance=0):
        super().__init__(balance)
        super().__init__(balance)
    def deposit(self, amount):
        if amount >0:
            self._balance +=amount 
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self._balance - amount >=-1000:
            self._balance - amount -= amount 
        else:
            print("limit exceeded")

    if __name__ =="__main__":
        savings = SavingAccount(10000)
        savings.deposit (2000)
        savings.withdraw(300)
        print(f"Savings Account Balance :{savings._get_balance()}")
    