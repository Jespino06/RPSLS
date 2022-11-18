from player import Player

class Human(Player):
    def __init__(self, name, gesture):
        self.name = name
        self.gesture = gesture
        pass

 
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