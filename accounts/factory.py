from accounts.account_manager import AccountManager
from accounts.savings_account import SavingsAccount
from accounts.checking_account import CheckingAccount
from accounts.credit_account import CreditAccount

class AccountFactory:

    """
    A factory class responsible for creating instances of different types of accounts.

    This class uses a static method to instantiate and return the appropriate account
    object based on the provided account type and parameters.

    Methods:
        create_account(account_type: str, **kwargs) -> AccountManager:
            Static method to create and return an account instance of the specified type.

    Raises:
        ValueError: If the account_type provided does not match any known account types.
    """
    @staticmethod
    def create_account(account_type: str, **kwargs) -> AccountManager:
        if account_type == "savings":
            return SavingsAccount(**kwargs)     
        elif account_type == "checking":
            return CheckingAccount(**kwargs)
        elif account_type == "credit":
            return CreditAccount(**kwargs)
        else:
            raise ValueError(f"Unknown account type: {account_type}")
        