from abc import ABC, abstractmethod

class AccountManager(ABC):

    """
Abstract base class to define the interface and common behavior
for managing different types of bank accounts.

"""
    @abstractmethod
    def account_type(self, account_type: str):
        pass
    @abstractmethod
    def deposit(self, amount: float):
        pass
    @abstractmethod
    def withdraw(self, amount: float):
        pass
    @abstractmethod 
    def get_balance(self) -> float:
        pass
    @abstractmethod
    def get_account_details(self) -> dict:
        pass


class SavingsAccount(AccountManager):
    """
Concrete implementation of a Savings Account inheriting from AccountManager.

Implements specific behavior for managing deposits, withdrawals,
balance inquiries, and account details relevant to savings accounts.
"""

    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.balance = initial_balance
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

class CheckingAccount(AccountManager):
    """
Concrete implementation of a Checking Account inheriting from AccountManager.

Implements specific behavior for managing deposits, withdrawals,
balance inquiries, and account details relevant to checking accounts.
"""

    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.balance = initial_balance
        self.account_type_name = "Checking"

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

