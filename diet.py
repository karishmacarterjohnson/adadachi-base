from constants import *

herbivore_foods = {
    "carrot sticks": 2,
    "mashed potatoes": 2, 
    "strawberries": 2 
}
carnivore_foods = {
    "steak": 2,
    "beef stew": 2, 
    "chicken": 2
}
omnivore_foods = {
    "carrot sticks": 1,
    "mashed potatoes": 1, 
    "strawberries": 1,
    "steak": 1,
    "beef stew": 1, 
    "chicken": 1
}


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
