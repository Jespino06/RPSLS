from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.human = Human('Player_one')
        self.ai = AI("Computer_one")
        pass

    def toss_phase(self):
        self.choice()
        