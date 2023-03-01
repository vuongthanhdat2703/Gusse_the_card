from Card import Card , group, suite
import random

class Desk:
    _cards: list[Card] = []

    def __init__(self) -> None:
        self.init_desk()
        pass

    def init_desk(sefl):
        for group_item in group.keys():
            for suite_item in suite.keys():
                card = Card(group_item,suite_item)
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