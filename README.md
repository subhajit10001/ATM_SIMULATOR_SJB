Defining the class or method for the ATM simulator functionality

Creating an ATM simulator involves designing a class with methods to handle various functionalities like account balance inquiry, withdrawal, deposit, and transfer

Key Points:
Initialization: The __init__ method sets up the initial balance and a list to store transaction history.
Check Balance: The check_balance method returns the current balance.
Deposit: The deposit method adds a specified amount to the balance if the amount is positive.
Withdraw: The withdraw method subtracts a specified amount from the balance if the amount is positive and there are sufficient funds.
Transfer: The transfer method moves a specified amount to another ATM instance if the amount is positive and there are sufficient funds.
Transaction History: The get_transaction_history method returns a list of all transactions made.
