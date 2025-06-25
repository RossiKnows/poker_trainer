from core.hand import *
from core.evaluator import HandEvaluator
from core.deck import Deck

evaluator = HandEvaluator()
deck = Deck()



hole_cards = PrivateHand()
hole_cards.receive_card(deck.deal_card())
hole_cards.receive_card(deck.deal_card())

community_cards= CommunityCards()

for _ in range(5):
    community_cards.add_card(deck.deal_card())

total_hand = TotalHand(hole_cards, community_cards)

print(total_hand)
print(evaluator.get_hand_name(total_hand))



# total_hand = TotalHand.from_strings(["Td", "Qd"], ["Jd", "4c", "Kd", "Ad", "4s"])
# five_card_hand = TotalHand.from_strings(["Td", "Qd"], ["Jd", "Kd", "Ad"])
