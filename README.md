1-Defining the class or method for the ATM simulator functionality

Creating an ATM simulator involves designing a class with methods to handle various functionalities like account balance inquiry, withdrawal, deposit, and transfer

Key Points:
Initialization: The __init__ method sets up the initial balance and a list to store transaction history.
Check Balance: The check_balance method returns the current balance.
Deposit: The deposit method adds a specified amount to the balance if the amount is positive.
Withdraw: The withdraw method subtracts a specified amount from the balance if the amount is positive and there are sufficient funds.
Transfer: The transfer method moves a specified amount to another ATM instance if the amount is positive and there are sufficient funds.
Transaction History: The get_transaction_history method returns a list of all transactions made.
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
