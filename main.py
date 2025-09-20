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

class CreditAccount(AccountManager):

    def __init__(self, account_number: str, credit_limit: float, interest_rate: float, initial_balance: float = 0.0):
        self.account_number = account_number
        self.balance = initial_balance
        self.credit_limit = credit_limit
        self.interest_rate = interest_rate
        self.account_type_name = "Credit"

    def account_type(self, account_type: str):
        return self.account_type_name

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= (self.balance + self.credit_limit):
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self) -> float:
        return self.balance

    def calculate_interest(self, months: int) -> float:
        """Calculate interest on the current balance over a given number of months.

        Args:
            months (int): Number of months to calculate interest for.

        Returns:
            float: Calculated interest amount.
        """
        monthly_rate = self.interest_rate / 12 / 100
        interest = self.balance * monthly_rate * months
        return interest if self.balance > 0 else 0.0 
    
    def apply_interest(self, months: int):
        """Apply calculated interest to the account balance.

        Args:
            months (int): Number of months to apply interest for.
        """
        interest = self.calculate_interest(months)
        if interest > 0:
            self.balance += interest
            print(f"Applied {interest} interest for {months} months. New balance is {self.balance}.")
        else:
            print("No interest applied as balance is non-positive.")

    def make_repayment(self, amount: float):
        """Make a repayment towards the credit account.

        Args:
            amount (float): Amount to repay.
        """
        if amount > 0:
            self.balance += amount
            print(f"Repayment of {amount} made. New balance is {self.balance}.")
        else:
            print("Repayment amount must be positive.")
            
 
    def check_credit_limit(self, amount):
        """Check if a withdrawal amount exceeds the credit limit.

        Args:
            amount (float): Amount to check against the credit limit.  
        Returns:
            bool: True if within limit, False otherwise.       
        """
        return amount <= (self.balance + self.credit_limit) 

    def get_account_details(self) -> dict:
        return {
            "account_number": self.account_number,
            "account_type": self.account_type_name,
            "balance": self.balance,
            "credit_limit": self.credit_limit,
            "interest_rate": self.interest_rate
        }   
  
