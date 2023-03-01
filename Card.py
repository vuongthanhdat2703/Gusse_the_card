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

class Card:
    _group: str
    _suite: str

    def __init__(self, group: str, suite: str) -> None:
        self._group = group
        self._suite = suite
        pass

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
