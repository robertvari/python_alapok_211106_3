class PlayerBase:
    def __init__(self, name):
        self._name = name
        self._credits = 0
        self._hand = []

    @property
    def name(self):
        return self._name

    @property
    def credits(self):
        return self._credits

    @property
    def hang(self):
        return self._hand

    def draw(self):
        print("PlayerBase draw")


class Player(PlayerBase):
    def draw(self):
        print(f"This is your turn {self._name}")
        input("Do you want to draw a card? (y/n)")


class AIPlayer(PlayerBase):
    pass


player1 = Player("Robert")
ai_player = AIPlayer("Csaba")

player1.draw()
ai_player.draw()