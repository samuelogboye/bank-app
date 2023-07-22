# Bank App Program
The BankAccount class is a simple Python class that simulates a bank account. It allows users to create an account, set a password, make deposits, withdraw funds, check their balance, apply interest, and even close the account. The class also supports multiple account holders, making it suitable for joint accounts.

## Features
Account Creation: Users can create a new bank account by providing an account number and the name of the primary account holder.

Password Setting: To ensure security, users are required to set a password for their account during the account creation process.

Deposits: Account holders can deposit funds into their account.

Withdrawals: Account holders can make withdrawals from their account, provided they enter the correct password and have sufficient funds.

Balance Display: Users can check their current account balance after providing the account password.

Interest Rate: The class supports an interest rate feature, where interest is applied to the account balance periodically.

Transaction History: The class keeps track of all deposits and withdrawals, allowing users to view their transaction history.

Joint Accounts: Multiple account holders can be added to the same account, making it suitable for joint account scenarios.

Account Closure: Users have the option to close their account, which will reset the balance, remove all account holders, and clear the transaction history.

Usage
```
Creating an Account:
acc_num = input("Enter your account number: ")
account_holder = input("Enter your name: ")

account1 = BankAccount(acc_num, account_holder)
account1.set_pass()
```
Making Deposits:
python
Copy code
account1.deposit()
Making Withdrawals:
python
Copy code
account1.withdraw()
Displaying Balance and Transaction History:
python
Copy code
account1.display_balance()
Adding Joint Account Holders:
python
Copy code
account_holder2 = input("Enter the name of the additional account holder: ")
account1.add_account_holder(account_holder2)
Applying Interest:
python
Copy code
account1.apply_interest()
Closing the Account:
python
Copy code
account1.close_account()
Note
Remember to modify the interest_rate variable inside the BankAccount class if you want to change the interest rate applied to the balance.

Author
This project is an opensource project, feel free to contribute

Enjoy managing your virtual bank account!
