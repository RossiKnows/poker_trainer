import random
from core.card import Card


class Deck:
    def __init__(self, shuffle=True):
        """
        Create a new deck of 52 cards.

        Args:
            shuffle (bool): Whether to shuffle the deck on creation.
        """
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """
        Deal (remove and return) the top card of the deck.

        Returns:
            Card: The card dealt.

        Raises:
            IndexError: If the deck is empty.
        """
        if len(self.cards) == 0:
            raise IndexError("Cannot deal from an empty deck.")
        return self.cards.pop()

    def cards_left(self) -> int:
        return len(self.cards)

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def reset(self, shuffle=True):
        """
        Reset the deck to a full 52 cards.

        Args:
            shuffle (bool): Whether to shuffle the new deck.
        """
        self.__init__(shuffle=shuffle)

    def __str__(self):
        """
        String representation of the deck.

        Returns:
            str: e.g., 'Deck(52 cards)'
        """
        return f"Deck ({self.cards_left()} cards)"

    def __repr__(self):
        """
        Developer-friendly representation.
        """
        return f"Deck({self.cards})"


# Test / demo
if __name__ == "__main__":
    deck = Deck()
    print(deck)
    card = deck.deal_card()
    # print(f"Dealt hand: {hand}")
    print(card)

    while not deck.is_empty():
        card = deck.deal_card()
        print(f"Dealt card: {card}")

    print(deck)
