from itertools import combinations
from typing import List, Tuple, Optional

from core.card import Card
from core.hand import TotalHand


class HandEvaluator:
    """
    Hand evaluator class for Texas Hold'em poker.
    Provides methods to evaluate and compare poker hands.
    """

    HAND_RANKS = {
        "High Card": 1,
        "Pair": 2,
        "Two Pair": 3,
        "Three of a Kind": 4,
        "Straight": 5,
        "Flush": 6,
        "Full House": 6,
        "Four of a Kind": 8,
        "Straight Flush": 9,
        "Royal Flush": 10,
    }

    def __init__(self):
        pass

    def evaluate_hand(self, hand: TotalHand) -> Tuple[int, List[int]]:
        """Finds strenght of hand between 5-7 cards.

        Returns:
        Tuple[int, List[int]]:
            - hand_rank: Integer representing hand strength (1=high card, 9=straight flush)
            - high_cards: List of card values in descending order for tiebreaking

        Examples:
            King-high flush: (6, [13, 12, 6, 4, 2])
            Pair of Aces with K-Q-J kickers: (2, [14, 13, 12, 11])
            Full house, Kings over Fives: (7, [13, 5])
        """
        raise NotImplementedError

    def _find_best_five_cards(self, cards: List[Card]) -> List[Card]:
        """Find strongest combination of five cards from up to 7."""
        raise NotImplementedError

    def _evaluate_five_card_hand(self, cards: List[Card]) -> Tuple[int, List[int]]:
        """
        Evaluates the strength of a 5 card poker hand.
        Returns a tuple of (hand_rank, high_cards) for comparison and display.

        Args:
        hand (TotalHand): Hand containing 5 cards to evaluate

        Returns:
        Tuple[int, List[int]]:
            - hand_rank: Integer representing hand strength (1=high card, 9=straight flush)
            - high_cards: List of card values in descending order for tiebreaking
        """
        values = sorted([card.get_rank_value() for card in cards], reverse=True)
        suits = [card.suit for card in cards]

        # Royal Flush

        # Straigh Flush

        # Four of a Kind

        # Full House

        # Flush
        is_flush = len(set(suits)) == 1
        print(is_flush)

        # Straight

        # Three of a kind

        # Two Pair

        # Pair
        # High Card
        raise NotImplementedError

    def compare_hands(self, hand1: TotalHand, hand2: TotalHand) -> int:
        raise NotImplementedError

    def get_hand_name(self, hand: TotalHand) -> str:
        raise NotImplementedError

    def _check_straight(self, values: List[int]) -> Tuple[bool, Optional[int]]:
        raise NotImplementedError


# Test code
if __name__ == "__main__":
    evaluator = HandEvaluator()
