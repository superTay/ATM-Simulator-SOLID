

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
