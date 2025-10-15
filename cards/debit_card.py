from cards.card import Card

class DebitCard(Card):
    """
    Represents a debit card, directly linked to a bank account.
    Operations are performed directly on the linked account's balance.
    """
    def card_type(self) -> str:
        return "debit"
