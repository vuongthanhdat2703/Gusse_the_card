from card import Card , group, suite
import random

class Desk:
    _cards: list[Card] = []
#try
    def __init__(self) -> None:
        try:
            self.init_desk()
        except Exception as a:
            print("Error occurred during initialization: ", a)

    def init_desk(sefl):
        for group_item in group.keys():
            for suite_item in suite.keys():
                card = Card(group_item, suite_item)
                sefl._cards.append(card)

    def pick_card(sefl):
        house_card_id = 0
        user_card_id = 0
    
        cards = sefl._cards

        while house_card_id == user_card_id:
            house_card_id = random.randint(0,52)
            user_card_id = random.randint(0,52)

        return{
            "house_card": cards[house_card_id],
            "player_card": cards[user_card_id]
        }