class Card:
    """
    A playing card with a suit and rank.
    """

    SUITS = ["♠", "♥", "♦", "♣"]
    SUIT_NAMES = ["Spades", "Hearts", "Diamonds", "Clubs"]

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    RANK_NAMES = [
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]
    RANK_VALUES = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def __init__(self, rank, suit):
        """
        Create a new card.

        Args:
            rank (str): The value of the card ('2'-'9', 'T', 'J', 'Q', 'K', 'A')
            suit (str): The suit of the card ('♠', '♥', '♦', '♣')

        Raises:
            ValueError: If rank or suit is invalid
        """
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}. Must be one of {self.RANKS}.")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}. Must be one of {self.SUITS}.")

        self.rank = rank
        self.suit = suit

    def __str__(self):
        """String representation of the card (e.g. 'A♠')"""
        return self.colorize()

    def __repr__(self):
        """Developer-friendly representation"""
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other):
        """Check if two cards are equal"""
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        """Compare cards by value (for sorting)"""
        if not isinstance(other, Card):
            return NotImplemented
        return self.get_rank_value() < other.get_rank_value()

    def __hash__(self):
        """Make card hashable for use in sets/dicts"""
        return hash((self.rank, self.suit))

    def colorize(self):
        """
        Return string representation of card with color.
        Hearts and Diamonds in red, others default.
        """
        rank_str = self.rank
        suit_str = self.suit
        if self.is_red():
            suit_str = f"\033[31m{self.suit}\033[0m"  # Alleen symbool rood kleuren
        return f"{rank_str}{suit_str}"

    def get_rank_value(self) -> int:
        """
        Get the numeric value of the rank.

        Returns:
            int: Numeric value (2-14, where A=14)
        """
        return self.RANK_VALUES[self.rank]

    def get_suit_name(self):
        """
        Get the full name of the suit.

        Returns:
            str: Full suit name (e.g. 'Spades')
        """
        suit_index = self.SUITS.index(self.suit)
        return self.SUIT_NAMES[suit_index]

    def get_rank_name(self):
        """
        Get the full name of the rank.

        Returns:
            str: Full rank name (e.g. 'Ace')
        """
        rank_index = self.RANKS.index(self.rank)
        return self.RANK_NAMES[rank_index]

    def get_full_name(self):
        """
        Get the full name of the card.

        Returns:
            str: Full name (e.g. 'Ace of Spades')
        """
        return f"{self.get_rank_name()} of {self.get_suit_name()}"

    def is_red(self) -> bool:
        """
        Check if the card is red.

        Returns:
            bool: True if Hearts or Diamonds
        """
        return self.suit in ["♥", "♦"]

    def is_black(self):
        """
        Check if the card is black.

        Returns:
            bool: True if Spades or Clubs
        """
        return self.suit in ["♠", "♣"]

    def is_face_card(self):
        """
        Check if the card is a face card.

        Returns:
            bool: True if Jack, Queen, or King
        """
        return self.rank in ["J", "Q", "K"]

    def is_ace(self):
        """
        Check if the card is an Ace.

        Returns:
            bool: True if Ace
        """
        return self.rank == "A"


# Helper function to create cards easily
def create_card(card_string):
    """
    Create a Card object from a string like 'A♠' or 'Kh'.

    Args:
        card_string (str): String representation of card (e.g. 'A♠', 'Kh', 'Ts')

    Returns:
        Card: Card object

    Raises:
        ValueError: If the string is not valid
    """
    if len(card_string) != 2:
        raise ValueError(f"Card string must be 2 characters, got: '{card_string}'")

    rank = card_string[0].upper()
    suit_char = card_string[1].lower()

    # Convert letter to symbol
    suit_mapping = {"s": "♠", "h": "♥", "d": "♦", "c": "♣"}

    if suit_char in suit_mapping:
        suit = suit_mapping[suit_char]
    elif card_string[1] in Card.SUITS:
        suit = card_string[1]
    else:
        raise ValueError(f"Unknown suit: {card_string[1]}")

    return Card(rank, suit)


# Test function (optional - for development)
if __name__ == "__main__":
    # Examples of usage
    ace_spades = Card("A", "♠")
    king_hearts = create_card("Kh")
    two_diamonds = create_card("2d")

    print(f"Card 1: {ace_spades}")
    print(f"Card 2: {king_hearts}")
    print(two_diamonds)

    set_of_cards = [ace_spades, two_diamonds]
    print(set_of_cards)
