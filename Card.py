group = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}

suite = {
    "Heart": 4,
    "Diamond": 3,
    "Club": 2,
    "Spade": 1
}

greatest_card = {
     "Black Joker" : 98,
     "Red Joker" :99
}


class Card:
    _group: str
    _suite: str


    def __init__(self, group: str, suite: str) -> None:
        self._group = group
        self._suite = suite
        # self._greatest_card = _greatest_card
        pass

    def __str__(self) -> str:
            return f"{self._group} of {self._suite}s"

    def is_greater_than(self, card) -> bool:
        this_group = self._group
        opponent_group = card._group
        if(group[this_group] < group[opponent_group]):
            return False
        elif (group[this_group] == group[opponent_group]):
            this_suite = self._suite
            opponent_suite = card._suite
            if(suite[this_suite] < suite[opponent_suite]):
                return False
            else:
                return True
        else:
            return True

# cards = []

# for group_value in group.keys():
#         for suite_value in suite.keys():
#             card = Card(group_value, suite_value)
#             cards.append(card)

# black_joker = Card("Black Joker","")
# red_joker = Card("Red Joker","")
# cards.append(black_joker)
# cards.append(red_joker)

# for card in cards:
#     print(str(card))
