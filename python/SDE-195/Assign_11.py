class BankAccount:
    # Create the balance variable
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        # Deposit function
        self.balance = self.balance + amount
        print("$" + str(amount) + " was added to your balance.")

    def withdraw(self, amount):
        # Withdrawal function
        newbalance = self.balance - amount
        # Checking if balance goes under $0
        if newbalance <= 0:
            print("You do not have $" + str(amount) + " to withdrawal")
        else:
            self.balance = newbalance
            print("$" + str(amount) + " was removed from your balance.")

class FeeAccount(BankAccount):
    def monthlyfee(self):
        self.balance = self.balance - 5

    def withdrawal(self, amount):
        # Withdrawal function with new fee
        newbalance = self.balance - amount - 2
        # Checking if balance goes under $0
        if newbalance <= 0:
            print("You do not have $" + str(amount+2) + " to withdrawal")
        else:
            self.balance = newbalance
            print("$" + str(amount+2) + " was removed from your balance.")

my_fee_account = FeeAccount()

# Doing the deposits and withdrawals
my_fee_account.deposit(1000)
my_fee_account.withdrawal(50)
my_fee_account.monthlyfee()

# Print total balance after
print("Your total balance is $" + str(my_fee_account.balance))
