from player import Player
from adadachi import Adadachi
from constants import *
from diet import *
import random

player = Player()

def display(statement):
    print(statement)


def create_adadachi():
    name = input(GET_NAME + "\n\t")
    pronouns = input(GET_PRONOUNS + "\n\t")
    foods = diet_chooser()
    games = player.inventory["games"]
    personality = {
        "fav_food": random.randint(0,len(foods)),
        "fav_game": random.randint(0,len(games)),
        "hates_food": random.randint(0,len(foods)),
        "hates_game": random.randint(0,len(games)),
    }
    player.adadachi = Adadachi(name, pronouns, personality)
    player.inventory["foods"] = foods

def start_game():
    display(TITLE)
    answer = input(GREETING)
    if answer.lower() == "y":
        create_adadachi()
        while player.adadachi.hunger < 5:
            option = input(OPTIONS).lower()

            if option == "s":
                player.get_status()
            elif option == "c":
                    player.clean()
            elif option == "f":
                if player.inventory["foods"]:
                    player.feed()
                else:
                    break
            elif option == "p":
                player.play_with_adadachi()
            elif option == "x":
                return display(EXIT)
        
        display(LOST)

# add poop graphic to clean()
# format poop level in clean()
# add food collection options
# upgrade food to dict
# settings menu

# fin
# add pronouns to game beginning
# add food preference
# determine food list based on this