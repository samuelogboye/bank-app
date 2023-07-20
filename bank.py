class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

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

    def withdraw(self):
        print("Withdrawal")
        amount = int(input("How much do you wish to withdraw?: "))
        if input("Enter your password: ") == self.passw:
            if self.balance >= amount:
                self.balance -= amount
                print("You have successfully withdrawn", amount)
                print("Your balance is", self.balance)
            else:
                print("Insufficient funds!")
        else:
            print("Incorrect Password")

    def display_balance(self):
        print("Display Account")
        if input("Enter your password: ") == self.passw:
            print("Account Number: ", self.account_number)
            print("Current Balance: ", self.balance)
        else:
            print("Incorrect Password")


acc_num = input("Enter your account number: ")
account1 = BankAccount(acc_num)
account1.set_pass()
account1.deposit()
account1.withdraw()
account1.display_balance()
