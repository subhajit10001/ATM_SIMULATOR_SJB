# -*- coding: utf-8 -*-
"""ATM SIMULATOR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xS0DGGVXLvZOLQTFtjJF8uJmNBLyEvit
"""

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return True
        return False

    def get_transaction_history(self):
        return self.transaction_history

class ATMSimulator:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin, initial_deposit=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, pin, initial_deposit)
            return True
        return False

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

def main():
    atm = ATMSimulator()
    while True:
        print("\nWelcome to the ATM Simulator")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            initial_deposit = float(input("Enter initial deposit: "))
            if atm.create_account(account_number, pin, initial_deposit):
                print("Account created successfully!")
            else:
                print("Account already exists!")

        elif choice == '2':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = atm.authenticate(account_number, pin)
            if account:
                print("Login successful!")
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transaction History")
                    print("5. Logout")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        print(f"Current Balance: ${account.check_balance()}")

                    elif choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        if account.deposit(amount):
                            print("Deposit successful!")
                        else:
                            print("Deposit failed!")

                    elif choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        if account.withdraw(amount):
                            print("Withdrawal successful!")
                        else:
                            print("Insufficient balance!")

                    elif choice == '4':
                        print("Transaction History:")
                        for transaction in account.get_transaction_history():
                            print(transaction)

                    elif choice == '5':
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice! Please try again.")
            else:
                print("Authentication failed! Please check your account number and PIN.")

        elif choice == '3':
            print("Thank you for using the ATM Simulator. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()