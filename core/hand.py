"""
Hand classes for Texas Hold'em poker game.
PrivataHand has a player's private hand (hole cards).
TotalHand has the total hand (hole + community cards.)
"""

from core.card import Card, create_card


class PrivateHand:
    """
    A player's private hand in Texas Hold'em (2 hole cards).
    """

    def __init__(self):
        self.cards: list[Card] = []

    def receive_card(self, card: Card) -> None:
        """
        Add a card to the private hand.

        Args:
            card (Card): The card to add.

        Raises:
            ValueError: If hand already has 2 cards.
        """
        if len(self.cards) >= 2:
            raise ValueError("Texas Hold'em hand can only have 2 hole cards.")
        self.cards.append(card)

    def clear(self) -> None:
        """
        Clear the hand.
        """
        self.cards.clear()

    def get_cards(self) -> list[Card]:
        """
        Return the cards in the hand.

        Returns:
            list of Card
        """
        return list(self.cards)

    def __len__(self) -> int:
        """
        Return the number of cards in the hand.
        """
        return len(self.cards)

    def __str__(self):
        """
        String representation of the hand.

        Returns:
            str: e.g., 'Hand: [Ah, Ks]'
        """
        return f"Private hand: [{', '.join(str(card) for card in self.cards)}]"

    def __repr__(self):
        """
        Developer-friendly representation.
        """
        return f"Hand({self.cards})"

    def sort(self, reverse=True):
        """
        Sort the hand by card rank.

        Args:
            reverse (bool): Sort high to low if True (default), else low to high.
        """
        self.cards.sort(reverse=reverse)


class CommunityCards:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to community cards.

        Args:
            card (Card): The card to add.

        Raises:
            ValueError: If hand already has 5 cards.
        """
        if len(self.cards) >= 5:
            raise ValueError("Texas Hold'em can only have 5 community cards.")
        self.cards.append(card)

    def clear(self) -> None:
        """
        Clear the community cards.
        """
        self.cards.clear()

    def get_cards(self) -> list[Card]:
        """
        Return the community cards.

        Returns:
            list of Card
        """
        return list(self.cards)

    def __len__(self) -> int:
        """
        Return the number of community cards.
        """
        return len(self.cards)

    def __str__(self):
        """
        String representation of the community cards.

        Returns:
            str: e.g., 'Com. Cards: [Ah, Ks]'
        """
        return f"Com. Cards: [{', '.join(str(card) for card in self.cards)}]"

    def __repr__(self):
        """
        Developer-friendly representation.
        """
        return f"Hand({self.cards})"


class TotalHand:
    def __init__(
        self, private_hand: PrivateHand, community_cards: CommunityCards
    ) -> None:
        self.private_hand = private_hand
        self.community_cards = community_cards

    @classmethod
    def from_strings(cls, private_cards: list[str], community_cards: list[str]):
        """
        Factory method to create TotalHand from card string lists.

        Args:
            private_cards: List of card strings for private hand (e.g., ["Td", "Qd"])
            community_cards: List of card strings for community cards (e.g., ["Jd", "4c", "Kd"])

        Returns:
            TotalHand: A new TotalHand instance

        Example:
            total_hand = TotalHand.from_strings(["Td", "Qd"], ["Jd", "4c", "Kd", "8s", "Ad"])
        """
        ph = PrivateHand()
        for card_str in private_cards:
            ph.receive_card(create_card(card_str))

        cc = CommunityCards()
        for card_str in community_cards:
            cc.add_card(create_card(card_str))

        return cls(ph, cc)

    @property
    def cards(self) -> list[Card]:
        cards = self.private_hand.cards + self.community_cards.cards
        cards.sort(reverse=True)
        return cards

    def sort(self, reverse=True):
        """
        Sort the total cards by card rank.

        Args:
            reverse (bool): Sort high to low if True (default), else low to high.
        """
        self.cards.sort(reverse=reverse)

    def __str__(self):
        """
        String representation of the total cards, sorted.

        Returns:
            str: e.g., 'Total Cards: [Ah, Ks, Td, 8s, 2s, 4d, 5d]'
        """
        return f"Total cards: [{', '.join(str(card) for card in self.cards)}]"

    def __repr__(self):
        """
        Developer-friendly representation.
        """
        return f"Total hand({self.cards})"


# Test / demo
if __name__ == "__main__":
    from core.deck import Deck

    deck = Deck()
    private_hand = PrivateHand()

    # Deal 2 cards into hand
    private_hand.receive_card(deck.deal_card())
    private_hand.receive_card(deck.deal_card())
    private_hand.sort()
    print(private_hand)

    # Deal 5 com. cards
    community_cards = CommunityCards()
    for _ in range(5):
        community_cards.add_card(deck.deal_card())
    print(community_cards)

    # Total hand
    total_hand = TotalHand(private_hand, community_cards)
    print(total_hand)
