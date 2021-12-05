import random
from characters import NPC, Enemy


class PlaceBase:
    def __init__(self):
        self.name = ""
        self.characters = []
        self.player = None

    def create_characters(self):
        self.characters.clear()
        for i in range(random.randint(1, 10)):
            self.characters.append(NPC().create())

    def enter(self, player):
        self.player = player


class Tavern(PlaceBase):
    def enter(self, player):
        super(Tavern, self).enter(player)
        print(f"Welcome in the tavern {player}. I you have gold, you are in the right place.")


class Arena(PlaceBase):
    def enter(self, player):
        super(Arena, self).enter(player)
        print(f"You are in the arena {player}. Fight for your life!")