from player import Player

class Human(Player):
    def __init__(self, name, gesture_list):
        self.name = name
        self.gesture_list = gesture_list 
        pass

 
    def num_of_players(self):
        while True:
            try:
                num = int(input("How many will be playing? Enter 1, 2, or 3. "))
            except ValueError:
                print("There was an error, please enter a single digit number. ")
                continue
            if num < 4 and num > 0:
                print(num)
                break
            else:
                print("There was an error, please enter a single digit number. ")
    
    
    def choice():
        while True:
            try:
                num = int(input("Enter a number from 1-5. "))
            except ValueError:
                print("There was an error, please enter a single digit number. ")
                continue
            if num< 6 and num > 0:
                print(num)
                break
            else:
                print("There was an error, please enter a single digit number. ")