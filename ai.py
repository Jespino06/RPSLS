from player import Player

class AI(Player):
    def __init__(self, name, gesture_list):
        self.name = name
        self.gesture_list = gesture_list()
        pass

import random

def spur_list(list):
        randomized_choice = (random.choice(list))
        return randomized_choice

randomly_selected_pick = spur_list(self.gesture_list)
print(randomly_selected_pick)


        
