from Match import Match
from Player import Player
import os

player = Player()
clear = lambda: os.system('cls')

def game():
    while(True):
        player.show_point()

        player_choice = input("Do you want to join a single match (y/n):")
        while (player_choice != "y" and player_choice != "n"):
            player_choice = input("Your choice (y/n):")

        if(player_choice == "n"):
            break

        success = player.join_match()
        clear()

        if(success == False):
            break

        match = Match()
        match.start()
        reward = match.get_reward()
        player.add_reward(reward)

        
if __name__ == '__main__':
    game()