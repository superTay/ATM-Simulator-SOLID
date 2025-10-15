from cards.card import Card
from cards.debit_card import DebitCard
from cards.credit_card import CreditCard

class CardFactory:
    """
    A factory class responsible for creating instances of different types of cards.
    This decouples the client code from the concrete card implementations.
    """
    @staticmethod
    def create_card(card_type: str, **kwargs) -> Card:
        """
        Static method to create and return a card instance of the specified type.

        Args:
            card_type (str): The type of card to create ('debit' or 'credit').
            **kwargs: The attributes required to initialize the card 
                      (e.g., card_number, pin, linked_account).

        Raises:
            ValueError: If the card_type provided is unknown.

        Returns:
            Card: An instance of a class that inherits from Card.
        """
        if card_type == "debit":
            return DebitCard(**kwargs)
        elif card_type == "credit":
            return CreditCard(**kwargs)
        else:
            raise ValueError(f"Unknown card type: {card_type}")
