from constants import *

herbivore_foods = ["carrot sticks", "mashed potatoes", "strawberries"]
carnivore_foods = ["steak", "beef stew", "chicken"]
omnivore_foods = herbivore_foods + carnivore_foods


def diet_chooser():
    foods = False
    while not foods:
        diet_choice = input(GET_DIET + "\n\t")
        if diet_choice.lower() == "h":
            foods = herbivore_foods
        elif diet_choice.lower() == "o":
            foods = omnivore_foods
        elif diet_choice.lower() == "c":
            foods = carnivore_foods
    return foods
    