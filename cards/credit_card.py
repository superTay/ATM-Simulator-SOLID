from cards.card import Card

class CreditCard(Card):
    """
    Represents a credit card.
    In a real scenario, this would have its own credit limit, balance, etc.
    For this simulation, it will behave similarly to a debit card but is identified
    as a 'credit' type.
    """
    def card_type(self) -> str:
        return "credit"
