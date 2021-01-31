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

my_account = BankAccount()

# Doing the deposits and withdrawals
my_account.deposit(1000)
my_account.withdraw(50)

# Print total balance after
print("Your total balance is $" + str(my_account.balance))
