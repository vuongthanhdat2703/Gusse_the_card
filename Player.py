class Player:
    _point:int = 60

    def __init__(self) -> None:
        pass
    
    def add_reward(self, rw: int):
        self._point += rw
        print(f"Reward was add {rw} point to your pocket, current {self._point}")

    def show_point(self):
        print(f"You have {self._point} !")

    def join_match(self) -> bool:
        if(self._point <= 30):
            print(f"You don't have enough point to join any match !")
            return False
        
        self._point -= 25
        print(f"Player joined ! current {self._point}")
        return True