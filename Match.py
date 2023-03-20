from card import Card
from desk import Desk
import os

desk = Desk()
clear = lambda: os.system('cls')
class Match:
    _reward = 0
    _wining_reward = 20
    _is_playing = True
    _round = 1

    def __init__(self):
        pass

    def display_card(sefl, player : str , card : Card):
        print(f'=> {player} card: [{card._group} {card._suite}] ')

    def add_reward(self):
        self._reward += self._wining_reward
        self._wining_reward *= 2

    def get_reward (sefl):
        return sefl._reward

    def start(self):
        while (self._is_playing):
            clear()
            print(f'==== Round {self._round} ====')
            picker = desk.pick_card()
            
            player_card = picker ['player_card']
            house_card = picker ['house_card']

            self.display_card('House', house_card)

            player_guest = input("Your guest (g/l): ")
            print(player_guest)
            while (player_guest != "g" and player_guest != "l"):
                player_guest = input("Your guest (g/l): ")


            self.display_card("You", player_card)

            is_greater_than = player_card.is_greater_than(house_card)

            if(is_greater_than == True and player_guest == "g"):
                self.add_reward()
                print("Correct !")
            elif (is_greater_than == False and player_guest == "l"):
                self.add_reward()
                print("Correct !")
            else:
                self._reward = 0
                print("Incorrect ! You lose")
                break

            print("==============================")

            player_choice = input("Do you want to continue (y/n):")
            while (player_choice != "y" and player_choice != "n"):
                player_choice = input("Your choice (y/n):")

            if(player_choice == "n" or self._reward  >= 1000):
                self._is_playing = False
