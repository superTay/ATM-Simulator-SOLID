from abc import ABC, abstractmethod
from accounts.account_manager import AccountManager

class Card(ABC):
    """
    Abstract base class to define the interface and common behavior
    for different types of bank cards.
    """
    def __init__(self, card_number: str, pin: str, linked_account: AccountManager):
        self._card_number = card_number
        self._pin = pin
        self._linked_account = linked_account

    @abstractmethod
    def card_type(self) -> str:
        """Returns the type of the card (e.g., 'debit', 'credit')."""
        pass

    def validate_pin(self, pin: str) -> bool:
        """Validates if the provided PIN matches the card's PIN."""
        return self._pin == pin

    def get_account(self) -> AccountManager:
        """Returns the account linked to this card."""
        return self._linked_account

    def get_card_details(self) -> dict:
        """Returns a dictionary with the card's public details."""
        return {
            "card_number": self._card_number[-4:],  # Show only last 4 digits
            "card_type": self.card_type()
        }
