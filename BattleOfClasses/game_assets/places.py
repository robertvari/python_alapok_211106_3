import random, time
from characters import NPC, Enemy, Player
from items import CommonItem, CommonWeapon, MagicWeapon


class PlaceBase:
    def __init__(self, name):
        self.name = name
        self.characters = []
        self.player = None

    def create_characters(self):
        for i in range(random.randint(1, 10)):
            self.characters.append(NPC().create())

    def enter(self, player):
        self.player = player


class Tavern(PlaceBase):
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

    def __init__(self, name):
        super(Tavern, self).__init__(name)
        self.inventory = []

        self.create_characters()
        self.create_inventory()

    def create_inventory(self):
        for _ in range(20):
            self.inventory.append(random.choice(self.basic_inventory_list))

    def show_inventory(self):
        for item in self.inventory:
            print(f"{item}\tPrice: {item.price}")

    def enter(self, player):
        super(Tavern, self).enter(player)
        print(f"Welcome in the tavern {player}. I you have gold, you are in the right place.")


class Arena(PlaceBase):
    def enter(self, player):
        super(Arena, self).enter(player)
        print(f"You are in the arena {player}. Fight for your life!")

        current_enemy = random.choice(self.characters)
        if current_enemy.right_hand:
            print(f"{current_enemy} attacks you with a {current_enemy.right_hand} in his right hand!")
        else:
            print(f"{current_enemy} attacks you!")

        while True:
            current_enemy.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player} died :(")
                break

            time.sleep(1)

            self.player.attack(current_enemy)
            if not current_enemy.is_alive():
                print(f"{current_enemy} died!!!")
                break

            time.sleep(1)

        if self.player.is_alive():
            print(f"{self.player} gets {current_enemy} items: {current_enemy.inventory}")
            self.player.inventory += current_enemy.inventory

            print(f"{self.player} wins {current_enemy.golds} golds.")
            self.player.golds += current_enemy.golds

            self.player.report()

    def create_characters(self):
        for i in range(random.randint(1, 10)):
            self.characters.append(Enemy().create())


if __name__ == '__main__':
    player = Player().create()

    tavern = Tavern("Black Horse Tavern")
    tavern.show_inventory()