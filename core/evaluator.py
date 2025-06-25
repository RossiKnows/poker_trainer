from itertools import combinations
from typing import List, Tuple, Optional

from core.card import Card
from core.hand import TotalHand

# TODO fixen dat get_hand_name de kaarten mooi op volgorde print.


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
        "Full House": 7,
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
        best_hand = (0, [0])
        for combination in combinations(hand.cards, 5):
            combination_list = list(combination)
            hand_rank = self._evaluate_five_card_hand(combination_list)
            if hand_rank[0] > best_hand[0]:
                best_hand = hand_rank
                continue

            elif hand_rank[0] < best_hand[0]:
                continue

            else:
                for i, score in enumerate(hand_rank[1]):
                    if score > hand_rank[1][i]:
                        best_hand = hand_rank
                        continue

                    elif score < hand_rank[1][i]:
                        continue

        return best_hand

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
        is_flush = len(set(suits)) == 1
        is_straight, straight_rank = self._check_straight(values)
        if is_flush:
            if is_straight:
                if straight_rank == 14:
                    return (10, values)

                # Straigh Flush
                elif is_flush and is_straight:
                    return (9, values)

            # Flush
            return (6, values)

        # Straight
        if is_straight:
            return (5, values)

        # Four of a Kind
        for combi in combinations(values, 4):
            combi_set = set(combi)
            if len(combi_set) == 1:
                four_of_a_kind = next(iter(combi_set))
                kicker = [v for v in values if v != combi]
                return (8, [four_of_a_kind, kicker[0]])

        # Full House
        for combi in combinations(values, 3):
            combi_set = set(combi)
            if len(combi_set) == 1:
                three_of_a_kind = next(iter(combi_set))
                remaining_two_cards = [v for v in values if v != combi[0]]
                if remaining_two_cards[0] == remaining_two_cards[1]:
                    return (7, [three_of_a_kind, remaining_two_cards[0]])

                # Three of a kind
                else:
                    return (4, [three_of_a_kind] + remaining_two_cards)

        # Two Pair
        for combi in combinations(values, 2):
            if combi[0] == combi[1]:
                remaining_three_cards = [v for v in values if v != combi[0]]
                if len(set(remaining_three_cards)) == 2:
                    for small_combi in combinations(remaining_three_cards, 2):
                        if small_combi[0] == small_combi[1]:
                            kicker = [
                                r for r in remaining_three_cards if r != small_combi[0]
                            ]
                            return (
                                3,
                                sorted([combi[0]] + [small_combi[0]], reverse=True)
                                + kicker,
                            )

                # Pair
                else:
                    return (2, [combi[0]] + remaining_three_cards)

        # High Card
        else:
            return (1, values)

    def compare_hands(self, hand1: TotalHand, hand2: TotalHand) -> int:
        """Compares strenght of two hands.
        Returns:    -1 if hand1 is stronger,
                    1 if hand2 is stronger and,
                    0 if it's a chop."""
        hand1_rank = self.evaluate_hand(hand1)
        hand2_rank = self.evaluate_hand(hand2)

        if hand1_rank[0] > hand2_rank[0]:
            return -1

        elif hand1_rank[0] < hand2_rank[0]:
            return 1

        else:
            for i, high_card_score in enumerate(hand1_rank[1]):
                if high_card_score > hand2_rank[1][i]:
                    return -1
                elif high_card_score < hand2_rank[1][i]:
                    return 1
            else:
                return 0

    def get_hand_name(self, hand: TotalHand) -> str:
        hand_rank, high_cards_values = self.evaluate_hand(hand)
        name = next(
            hand_name
            for hand_name, rank in self.HAND_RANKS.items()
            if rank == hand_rank
        )

        all_high_cards = []
        for high_cards_value in high_cards_values:
            high_card_name = [
                card_name
                for card_name, value in Card.RANK_VALUES.items()
                if value == high_cards_value
            ]
            all_high_cards.extend(high_card_name)
        return f"{name} with {', '.join(all_high_cards)}."  # TODO hier misschien de kaarten met symbool printen.

    def _check_straight(self, values: List[int]) -> Tuple[bool, Optional[int]]:
        unique_values = list(set(values))
        if len(unique_values) == 5:
            difference = 0

            for i in range(1, len(unique_values)):
                difference += unique_values[i] - unique_values[i - 1]
            if difference == 4:
                return (True, unique_values[-1])
            else:
                return (False, None)

        else:
            return (False, None)


# Test code
if __name__ == "__main__":
    evaluator = HandEvaluator()

    total_hand = TotalHand.from_strings(["Td", "Qd"], ["9d", "4c", "Kd", "Ad", "4s"])
    five_card_hand1 = TotalHand.from_strings(["5d", "5h"], ["6s", "th", "td"])
    five_card_hand2 = TotalHand.from_strings(["5d", "5h"], ["6s", "th", "td"])
    # print(evaluator.evaluate_hand(total_hand))
    print(evaluator.compare_hands(five_card_hand1, five_card_hand2))
