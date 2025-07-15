"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Create a class BankAccount with:
data members (attributes) (Initialized using __init__):
    account_holder_name (str)
    current_balance (float)

Methods:
    deposit(amount): Add amount to current_balance.
    withdraw(amount): Subtract if current_balance is sufficient.
    check_balance(): Return current_balance.
    display_summary(): Print holder name and current_balance.
"""
# SOLUTION

class BankAccount:
    def __init__(self, account_holder_name, current_balance):  # <-- fixed here
        self.account_holder_name = account_holder_name
        self.current_balance = current_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.current_balance}")

    def withdraw(self, amount):
        if amount <= self.current_balance:
            self.current_balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.current_balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        return self.current_balance

    def display_summary(self):
        print(f"Holder name: {self.account_holder_name}")
        print(f"Current balance: ₹{self.current_balance}")


# Testing the class
acc = BankAccount("Rohan", 10000.0)

acc.deposit(30000)
acc.withdraw(20000)
print("Balance:", acc.check_balance())
acc.display_summary()
