class CharacterBase:
    def __init__(self):
        self.inventory = []
        self.max_weight = 0
        self.race = None
        self.golds = 0

        # combat stats
        self.strength = 0
        self.max_HP = 0
        self.current_HP = 0


class Player(CharacterBase):
    pass


class Enemy(CharacterBase):
    pass


class NPC(CharacterBase):
    pass