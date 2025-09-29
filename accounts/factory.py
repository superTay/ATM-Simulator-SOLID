from accounts.account_manager import AccountManager
from accounts.savings_account import SavingsAccount
from accounts.checking_account import CheckingAccount
from accounts.credit_account import CreditAccount

class AccountFactory:
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
        