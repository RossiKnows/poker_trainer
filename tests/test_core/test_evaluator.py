from core.hand import *
from core.evaluator import HandEvaluator

evaluator = HandEvaluator()

total_hand = TotalHand.from_strings(["Td", "Qd"], ["Jd", "4c", "Kd", "Ad", "4s"])
five_card_hand = TotalHand.from_strings(["Td", "Qd"], ["Jd", "Kd", "Ad"])
evaluator._evaluate_five_card_hand(five_card_hand.cards)
