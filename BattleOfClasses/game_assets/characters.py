import random


class CharacterBase:
    races = {
        "human": {"strength": 50, "max_HP": 100, "max_weight": 50},
        "ork": {"strength": 130, "max_HP": 200, "max_weight": 100},
        "elf": {"strength": 60, "max_HP": 100, "max_weight": 60},
        "dwarf": {"strength": 130, "max_HP": 230, "max_weight": 150},
    }

    def __init__(self):
        self.inventory = []
        self.max_weight = 0
        self.race = None
        self.golds = 0
        self.name = None

        # combat stats
        self.strength = 0
        self.max_HP = 0
        self.current_HP = 0

    def create(self):
        self.name = self.get_fantasy_name()
        self.race = random.choice(list(self.races))
        self.setup_race()

        return self

    def setup_race(self):
        self.strength = self.races[self.race]["strength"]
        self.max_HP = self.races[self.race]["max_HP"]
        self.current_HP = self.max_HP
        self.golds = random.randint(0, 100)
        self.max_weight = self.races[self.race]["max_weight"]

    def report(self):
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Strength: {self.strength}")
        print(f"Max HP: {self.max_HP}")
        print(f"Max Weight: {self.max_weight}")
        print(f"Golds: {self.golds}")
        print(f"Inventory: {self.inventory}")

    @staticmethod
    def get_fantasy_name():
        FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
                 'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
                 'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
                 'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
                 'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

        SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
                  'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
                  'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
                  'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
                  'wain', 'wan', 'win', 'wise', 'ya']

        return f"{random.choice(FIRST)}{random.choice(SECOND)}"


class Player(CharacterBase):
    def create(self):
        self.name = input("What is your name?")
        race = input(f"What is your race? {list(self.races)}")

        while race not in self.races:
            print("Wrong choice.")
            race = input(f"What is your race? {list(self.races)}")

        self.race = race
        self.setup_race()


class Enemy(CharacterBase):
    pass


class NPC(CharacterBase):
    pass


if __name__ == '__main__':
    enemy = Enemy().create()
    enemy.report()

    npc = NPC().create()
    npc.report()