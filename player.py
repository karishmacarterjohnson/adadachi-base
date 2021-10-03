from constants import *
from adadachi import Adadachi
import random

class Player():
    def __init__(self):
    
        self.adadachi = None
        self.inventory = {
            "games": ["hide-n-seek", "tag", "go fish", "red rover"],
            "foods": ["banana cream pie", "carrot sticks", "mashed potatoes", "mac 'n cheese", "tater tots", "chocolate cake", "strawberries", "fried rice"],
        }
       
    ### decorator for pre & post stringing

    def get_status(self):
        status_entry = STATUS
        features = ['name', 'pronouns', 'hunger', 'happiness', 'poop_lvl']
        #avail_spaces = 42 #50 - '^  '*2 - ': '
        linebreak = '^' + 48*' ' + '^\n' 
        space_req = len(max(features, key = len)) + 1
        space_rem = 42 - space_req
        for feature in features:
            status_entry += linebreak
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
            keep_pooping = input()

    def feed(self):

        self.inventory["foods"]
        # 
        pass
