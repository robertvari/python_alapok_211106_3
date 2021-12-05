import random
from items import CommonItem, CommonWeapon, MagicWeapon, WeaponBase


class CharacterBase:
    races = {
        "human": {"strength": 50, "max_HP": 100, "max_weight": 50},
        "ork": {"strength": 130, "max_HP": 200, "max_weight": 100},
        "elf": {"strength": 60, "max_HP": 100, "max_weight": 60},
        "dwarf": {"strength": 130, "max_HP": 230, "max_weight": 150},
    }

    basic_inventory_list = [
        CommonItem("Cup of beer", price=5, weight=5, health_modifier=5),
        CommonItem("Cheese", price=10, weight=3, health_modifier=20),
        CommonItem("Slice of Bread", price=3, weight=2, health_modifier=20),
        CommonWeapon("Sword", 20, 20, 10),
        CommonWeapon("Axe", 30, 35, 20),
        CommonWeapon("Hammer", 30, 35, 20),
        CommonWeapon("Spear", 30, 35, 20),
        MagicWeapon("Magic Sword", 60, 15, 50, 30),
    ]

    def __init__(self):
        self.inventory = []
        self.max_weight = 0
        self.race = None
        self.golds = 0
        self.name = None
        self.right_hand = None

        # combat stats
        self.strength = 0
        self.max_HP = 0
        self.current_HP = 0

    def create(self):
        self.name = self.get_fantasy_name()
        self.race = random.choice(list(self.races))
        self.setup_race()
        self.generate_inventory()

        return self

    def attack(self, other):
        print(f"{self.name} attacks {other}")
        attack_strength = random.randint(0, self.strength)

        if self.right_hand:
            attack_strength += self.right_hand.strength_modifier

        if attack_strength == 0:
            print(f"{self.name} misses...")
        else:
            print(f"{self.name} hits {other} with {attack_strength}")
            other.current_HP -= attack_strength

    def is_alive(self):
        return self.current_HP > 0

    def generate_inventory(self):
        for _ in range(random.randint(0, 3)):
            item = random.choice(self.basic_inventory_list)
            self.inventory.append(item)

        for item in self.inventory:
            if isinstance(item, WeaponBase):
                self.right_hand = item
                break

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

    def __repr__(self):
        return self.name


class Player(CharacterBase):
    def create(self):
        # todo replace this with input()
        self.name = "Robert"
        # race = input(f"What is your race? {list(self.races)}")
        race = "ork"

        # while race not in self.races:
        #     print("Wrong choice.")
        #     # race = input(f"What is your race? {list(self.races)}")

        self.race = race
        self.setup_race()

        return self


class Enemy(CharacterBase):
    pass


class NPC(CharacterBase):
    pass


if __name__ == '__main__':
    for _ in range(10):
        enemy = Enemy().create()
        print(enemy.name, enemy.right_hand)
