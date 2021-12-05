class ItemBase:
    def __init__(self, name, price, weight, health_modifier=0):
        self.name = name
        self.price = price
        self.weight = weight
        self.health_modifier = health_modifier

    def use(self):
        print("ItemBase use called")

    def report(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Weight: {self.weight}")
        print(f"Health modifier: {self.health_modifier}")

    def __repr__(self):
        return self.name


class CommonItem(ItemBase):
    pass


class WeaponBase(ItemBase):
    def __init__(self, name, price, weight, strength_modifier, health_modifier=0):
        super().__init__(name, price, weight, health_modifier)

        self.strength_modifier = strength_modifier

    def report(self):
        super().report()
        print(f"Strength modifier: {self.strength_modifier}")


class CommonWeapon(WeaponBase):
    pass


class MagicWeapon(WeaponBase):
    def __init__(self, name, price, weight, strength_modifier, magic_strength, health_modifier=0):
        super().__init__(name, price, weight, strength_modifier, health_modifier)
        self.magic_strength = magic_strength

    def report(self):
        super(MagicWeapon, self).report()
        print(f"Magic strength: {self.magic_strength}")


if __name__ == '__main__':
    cup_of_beer = CommonItem("Cup of beer", price=5, weight=5, health_modifier=5)
    cheese = CommonItem("Cheese", price=10, weight=3, health_modifier=20)
    bread = CommonItem("Slice of Bread", price=3, weight=2, health_modifier=20)

    sword = CommonWeapon(
        name="Sword",
        price=30,
        weight=20,
        strength_modifier=20
    )

    magic_sword = MagicWeapon(
        name="Magic Sword",
        price=150,
        weight=10,
        strength_modifier=40,
        magic_strength=30
    )

    inventory = [cup_of_beer, cheese, bread, sword, magic_sword]

    sword.report()
    print("-"*50)
    magic_sword.report()