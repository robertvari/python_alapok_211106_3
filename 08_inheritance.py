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


class Player(PlayerBase):
    pass


class AIPlayer(PlayerBase):
    pass


player1 = Player("Robert")
ai_player = AIPlayer("Csaba")

print(player1.name)
print(ai_player.name)