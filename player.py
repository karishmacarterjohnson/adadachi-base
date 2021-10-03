from constants import *
from adadachi import Adadachi
from helper import *
import random

class Player():
    def __init__(self):
        self.adadachi = None
        self.inventory = {
            "games": ["hide-n-seek", "tag", "go fish", "red rover"],
            "foods": None
        }
    


    ### decorator for pre & post stringing

    def get_status(self):
        status_entry = STATUS
        features = ['name', 'pronouns', 'hunger', 'happiness', 'poop_lvl']
        space_req = len(max(features, key = len)) + 1
        space_rem = 42 - space_req
        for feature in features:
            status_entry += LINEBREAK
            status_entry += '^  ' \
                         + feature.upper() + (space_req - len(feature))*' ' + ': ' \
                         + str(getattr(self.adadachi, feature)) \
                         + (space_rem - len(str(getattr(self.adadachi, feature))))*' ' \
                         +  '  ^\n'
        print(status_entry)   



    def clean(self):
        keep_pooping = True
        while self.adadachi.poop_lvl > 0 and keep_pooping:
            self.adadachi.poop_lvl -= 1
            print(POOP_STATUS_TOP)
            print(f'^  ') 
            print(self.adadachi.poop_lvl)
            ## add poop_lvl formatting
            print(POOP_STATUS_BOT)
            keep_pooping = continue_activity()  
            

    def feed(self):
        print(self.inventory["foods"])
        keep_eating = True
        while len(self.inventory["foods"]) > 0 and keep_eating:
            # display options
            print(FOOD_MENU + "\n")
            for key, value in self.inventory["foods"].items():
                print(LINEBREAK)
                print(key, value) # format
            food_choice = input("Enter name of the food").lower() # format
            try: 
                if self.inventory["foods"][food_choice] > 1:
                    self.inventory["foods"][food_choice] -= 1
                    self.hunger -=1 
                else:
                    self.inventory["foods"].pop(food_choice)  
                ### add ascii to show success
                print("yum")       
            except:
                print("you don't have that food. you can try again.")
            # cute eating ascii art
            keep_eating = continue_activity()
