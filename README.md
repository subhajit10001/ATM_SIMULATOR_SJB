1-Defining the class or method for the ATM simulator functionality

Creating an ATM simulator involves designing a class with methods to handle various functionalities like account balance inquiry, withdrawal, deposit, and transfer

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return f"Your balance is ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            return f"${amount:.2f} deposited. New balance: ${self.balance:.2f}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew: ${amount:.2f}")
                return f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}"
            return "Insufficient funds"
        return "Invalid withdrawal amount"

    def transfer(self, amount, other_account):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                other_account.balance += amount
                self.transaction_history.append(f"Transferred: ${amount:.2f} to account {id(other_account)}")
                other_account.transaction_history.append(f"Received: ${amount:.2f} from account {id(self)}")
                return f"${amount:.2f} transferred. New balance: ${self.balance:.2f}"
            return "Insufficient funds"
        return "Invalid transfer amount"

    def get_transaction_history(self):
        return "\n".join(self.transaction_history) if self.transaction_history else "No transactions yet."

# Example usage:
# Create two ATM instances
atm1 = ATM(1000)
atm2 = ATM(500)

# Check balance
print(atm1.check_balance())  # Output: Your balance is $1000.00

# Deposit money
print(atm1.deposit(200))  # Output: $200.00 deposited. New balance: $1200.00

# Withdraw money
print(atm1.withdraw(300))  # Output: $300.00 withdrawn. New balance: $900.00

# Transfer money
print(atm1.transfer(100, atm2))  # Output: $100.00 transferred. New balance: $800.00

# Print transaction history
print(atm1.get_transaction_history())  
# Output:
# Deposited: $200.00
# Withdrew: $300.00
# Transferred: $100.00 to account <atm2_id>

print(atm2.get_transaction_history())  
# Output:
# Received: $100.00 from account <atm1_id>


Key Points:
Initialization: The __init__ method sets up the initial balance and a list to store transaction history.
Check Balance: The check_balance method returns the current balance.
Deposit: The deposit method adds a specified amount to the balance if the amount is positive.
Withdraw: The withdraw method subtracts a specified amount from the balance if the amount is positive and there are sufficient funds.
Transfer: The transfer method moves a specified amount to another ATM instance if the amount is positive and there are sufficient funds.
Transaction History: The get_transaction_history method returns a list of all transactions made.


2-Defining multiple conditions for selecting at least 4 ATM functionalities 

When defining multiple conditions for selecting at least four ATM functionalities, you can incorporate various checks and validations to ensure robust functionality. Here’s how you can expand the ATM class to include more complex conditions for its methods.

Additional Functionalities:
PIN Authentication: Ensure the user is authenticated before performing transactions.
Daily Withdrawal Limit: Implement a daily limit for withdrawals.
Minimum Balance Requirement: Ensure the account does not go below a minimum balance.
Fee for Specific Transactions: Apply a fee for certain types of transactions.
Enhanced ATM Class with Conditions:
class ATM:
    def __init__(self, balance=0, pin='0000'):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []
        self.daily_withdrawal_amount = 0
        self.daily_withdrawal_limit = 1000  # Example limit
        self.minimum_balance = 100  # Example minimum balance
        self.transaction_fee = 2.50  # Example transaction fee

    def authenticate(self, pin):
        return self.pin == pin

    def check_balance(self, pin):
        if self.authenticate(pin):
            return f"Your balance is ${self.balance:.2f}"
        return "Authentication failed"

    def deposit(self, amount, pin):
        if self.authenticate(pin):
            if amount > 0:
                self.balance += amount
                self.transaction_history.append(f"Deposited: ${amount:.2f}")
                return f"${amount:.2f} deposited. New balance: ${self.balance:.2f}"
            return "Invalid deposit amount"
        return "Authentication failed"

    def withdraw(self, amount, pin):
        if self.authenticate(pin):
            if amount > 0:
                if amount <= self.balance:
                    if self.daily_withdrawal_amount + amount <= self.daily_withdrawal_limit:
                        if self.balance - amount >= self.minimum_balance:
                            self.balance -= amount
                            self.daily_withdrawal_amount += amount
                            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
                            return f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}"
                        return f"Withdrawal would breach minimum balance of ${self.minimum_balance:.2f}"
                    return f"Daily withdrawal limit of ${self.daily_withdrawal_limit:.2f} exceeded"
                return "Insufficient funds"
            return "Invalid withdrawal amount"
        return "Authentication failed"

    def transfer(self, amount, other_account, pin):
        if self.authenticate(pin):
            if amount > 0:
                if amount <= self.balance:
                    if self.balance - amount >= self.minimum_balance:
                        self.balance -= amount
                        other_account.balance += amount
                        self.transaction_history.append(f"Transferred: ${amount:.2f} to account {id(other_account)}")
                        other_account.transaction_history.append(f"Received: ${amount:.2f} from account {id(self)}")
                        return f"${amount:.2f} transferred. New balance: ${self.balance:.2f}"
                    return f"Transfer would breach minimum balance of ${self.minimum_balance:.2f}"
                return "Insufficient funds"
            return "Invalid transfer amount"
        return "Authentication failed"

    def apply_transaction_fee(self, pin):
        if self.authenticate(pin):
            if self.balance >= self.transaction_fee:
                self.balance -= self.transaction_fee
                self.transaction_history.append(f"Transaction fee applied: ${self.transaction_fee:.2f}")
                return f"Transaction fee of ${self.transaction_fee:.2f} applied. New balance: ${self.balance:.2f}"
            return "Insufficient funds for transaction fee"
        return "Authentication failed"

    def get_transaction_history(self, pin):
        if self.authenticate(pin):
            return "\n".join(self.transaction_history) if self.transaction_history else "No transactions yet."
        return "Authentication failed"

# Example usage:
# Create two ATM instances
atm1 = ATM(1000, pin='1234')
atm2 = ATM(500, pin='5678')

# Authenticate and Check balance
print(atm1.check_balance('1234'))  # Output: Your balance is $1000.00

# Authenticate and Deposit money
print(atm1.deposit(200, '1234'))  # Output: $200.00 deposited. New balance: $1200.00

# Authenticate and Withdraw money
print(atm1.withdraw(300, '1234'))  # Output: $300.00 withdrawn. New balance: $900.00

# Authenticate and Transfer money
print(atm1.transfer(100, atm2, '1234'))  # Output: $100.00 transferred. New balance: $800.00

# Apply transaction fee
print(atm1.apply_transaction_fee('1234'))  # Output: Transaction fee of $2.50 applied. New balance: $797.50

# Authenticate and Print transaction history
print(atm1.get_transaction_history('1234'))  
# Output:
# Deposited: $200.00
# Withdrew: $300.00
# Transferred: $100.00 to account <atm2_id>
# Transaction fee applied: $2.50
Key Points:
PIN Authentication: The authenticate method checks if the provided PIN matches the account PIN.
Daily Withdrawal Limit: The withdraw method includes a condition to ensure withdrawals do not exceed a daily limit.
Minimum Balance Requirement: Both the withdraw and transfer methods ensure transactions do not breach a specified minimum balance.
Transaction Fee: The apply_transaction_fee method deducts a fee for transactions if there are sufficient funds.
This enhanced ATM class adds more complexity and ensures secure and regulated handling of transactions, suitable for more realistic scenarios.

3-Defining the main method and calling the class or method in the main method  

To define the main method and call the class methods within it, you can follow a common structure used in Python. The main method serves as the entry point of the program, where the ATM class is instantiated, and its methods are invoked based on user input or predefined logic.

Here's an example:

class ATM:
    def __init__(self, balance=0, pin='0000'):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []
        self.daily_withdrawal_amount = 0
        self.daily_withdrawal_limit = 1000  # Example limit
        self.minimum_balance = 100  # Example minimum balance
        self.transaction_fee = 2.50  # Example transaction fee

    def authenticate(self, pin):
        return self.pin == pin

    def check_balance(self, pin):
        if self.authenticate(pin):
            return f"Your balance is ${self.balance:.2f}"
        return "Authentication failed"

    def deposit(self, amount, pin):
        if self.authenticate(pin):
            if amount > 0:
                self.balance += amount
                self.transaction_history.append(f"Deposited: ${amount:.2f}")
                return f"${amount:.2f} deposited. New balance: ${self.balance:.2f}"
            return "Invalid deposit amount"
        return "Authentication failed"

    def withdraw(self, amount, pin):
        if self.authenticate(pin):
            if amount > 0:
                if amount <= self.balance:
                    if self.daily_withdrawal_amount + amount <= self.daily_withdrawal_limit:
                        if self.balance - amount >= self.minimum_balance:
                            self.balance -= amount
                            self.daily_withdrawal_amount += amount
                            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
                            return f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}"
                        return f"Withdrawal would breach minimum balance of ${self.minimum_balance:.2f}"
                    return f"Daily withdrawal limit of ${self.daily_withdrawal_limit:.2f} exceeded"
                return "Insufficient funds"
            return "Invalid withdrawal amount"
        return "Authentication failed"

    def transfer(self, amount, other_account, pin):
        if self.authenticate(pin):
            if amount > 0:
                if amount <= self.balance:
                    if self.balance - amount >= self.minimum_balance:
                        self.balance -= amount
                        other_account.balance += amount
                        self.transaction_history.append(f"Transferred: ${amount:.2f} to account {id(other_account)}")
                        other_account.transaction_history.append(f"Received: ${amount:.2f} from account {id(self)}")
                        return f"${amount:.2f} transferred. New balance: ${self.balance:.2f}"
                    return f"Transfer would breach minimum balance of ${self.minimum_balance:.2f}"
                return "Insufficient funds"
            return "Invalid transfer amount"
        return "Authentication failed"

    def apply_transaction_fee(self, pin):
        if self.authenticate(pin):
            if self.balance >= self.transaction_fee:
                self.balance -= self.transaction_fee
                self.transaction_history.append(f"Transaction fee applied: ${self.transaction_fee:.2f}")
                return f"Transaction fee of ${self.transaction_fee:.2f} applied. New balance: ${self.balance:.2f}"
            return "Insufficient funds for transaction fee"
        return "Authentication failed"

    def get_transaction_history(self, pin):
        if self.authenticate(pin):
            return "\n".join(self.transaction_history) if self.transaction_history else "No transactions yet."
        return "Authentication failed"


def main():
    # Create two ATM instances
    atm1 = ATM(1000, pin='1234')
    atm2 = ATM(500, pin='5678')

    # Interact with ATM 1
    print(atm1.check_balance('1234'))  # Check balance
    print(atm1.deposit(200, '1234'))  # Deposit money
    print(atm1.withdraw(300, '1234'))  # Withdraw money
    print(atm1.transfer(100, atm2, '1234'))  # Transfer money
    print(atm1.apply_transaction_fee('1234'))  # Apply transaction fee
    print(atm1.get_transaction_history('1234'))  # Print transaction history

    # Interact with ATM 2
    print(atm2.check_balance('5678'))  # Check balance
    print(atm2.get_transaction_history('5678'))  # Print transaction history


if __name__ == "__main__":
    main()
```

### Key Points:
- **Class Definition**: The `ATM` class includes methods for checking balance, depositing, withdrawing, transferring money, applying transaction fees, and printing transaction history.
- **Main Method**: The `main` function creates instances of the `ATM` class and interacts with them by calling various methods.
- **Condition Check**: Methods within the `ATM` class include conditions for authentication, daily withdrawal limits, minimum balance requirements, and transaction fees.
- **Execution**: The `if __name__ == "__main__": main()` construct ensures that the `main` function is executed when the script is run directly.

This structure ensures the ATM simulator is organized, maintainable, and ready for further development or integration into a larger system.









