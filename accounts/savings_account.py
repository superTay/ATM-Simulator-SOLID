from accounts.account_manager import AccountManager


class SavingsAccount(AccountManager):
    """
Concrete implementation of a Savings Account inheriting from AccountManager.

Implements specific behavior for managing deposits, withdrawals,
balance inquiries, and account details relevant to savings accounts.
"""

    def __init__(self, account_holder: str, account_number: str, balance: float = 0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.account_type_name = "Savings"

    def account_type(self, account_type: str):
        return self.account_type_name

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self) -> float:
        return self.balance

    def get_account_details(self) -> dict:
        return {
            "account_number": self.account_number,
            "account_type": self.account_type_name,
            "balance": self.balance
        }