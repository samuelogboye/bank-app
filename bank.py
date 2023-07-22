lass BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holders = [account_holder]
        self.balance = 0
        self.transaction_history = []
        # 2% interest rate per period (you can adjust this value)
        self.interest_rate = 0.02

    def add_account_holder(self, account_holder):
        self.account_holders.append(account_holder)

    def remove_account_holder(self, account_holder):
        if account_holder in self.account_holders:
            self.account_holders.remove(account_holder)

    def set_pass(self):
        print("Set Password")
        while True:
            a = input("Enter your password: ")
            b = input("Confirm your password: ")
            if a == b:
                self.passw = a
                print("Password successfuly set")
                break
            else:
                print("Not Same, Try again")

    def deposit(self):
        print("Deposit")
        amount = int(input("How much do you wish to deposit?: "))
        self.balance += amount
        print("You have successfully deposit", amount)
        print("Your balance is", self.balance)
        self.transaction_history.append(f"Deposit: {amount}")

    def withdraw(self):
        print("Withdrawal")
        amount = int(input("How much do you wish to withdraw?: "))
        if input("Enter your password: ") == self.passw:
            if self.balance >= amount:
                self.balance -= amount
                print("You have successfully withdrawn", amount)
                print("Your balance is", self.balance)
                self.transaction_history.append(f"Withdrawal: {amount}")
            else:
                print("Insufficient funds!")
        else:
            print("Incorrect Password")

    def display_balance(self):
        print("Display Account")
        if input("Enter your password: ") == self.passw:
            print("Account Number: ", self.account_number)
            print("Current Balance: ", self.balance)
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("Incorrect Password")

    def apply_interest(self):
        # Calculate and add interest to the balance
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print("Interest Applied:", interest_amount)

    def close_account(self):
        self.balance = 0
        self.account_holders = []
        self.transaction_history = []
        print("Account closed.")


# Example usage:
acc_num = input("Enter your account number: ")
account_holder = input("Enter your name: ")

account1 = BankAccount(acc_num, account_holder)
account1.set_pass()

account1.deposit()
account1.withdraw()
account1.display_balance()

# Adding another account holder
account_holder2 = input("Enter the name of the additional account holder: ")
account1.add_account_holder(account_holder2)

# Applying interest
account1.apply_interest()

# Closing the account
account1.close_account()
