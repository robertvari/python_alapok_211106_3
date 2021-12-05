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


class Common(ItemBase):
    pass


class WeaponBase(ItemBase):
    def __init__(self, name, price, weight, health_modifier=0, strength_modifier=0):
        super().__init__(name, price, weight, health_modifier)

        self.strength_modifier = strength_modifier

    def report(self):
        super().report()
        print(f"Strength modifier: {self.strength_modifier}")


class CommonWeapon(WeaponBase):
    pass


class MagicWeapon(WeaponBase):
    def __init__(self, name, price, weight, health_modifier=0, strength_modifier=0, magic_strength=0):
        super().__init__(name, price, weight, health_modifier, strength_modifier)
        self.magic_strength = magic_strength

    def report(self):
        super(MagicWeapon, self).report()
        print(f"Magic strength: {self.magic_strength}")


if __name__ == '__main__':
    cup_of_beer = Common("Cup of beer", price=5, weight=5, health_modifier=5)
    cheese = Common("Cheese", price=10, weight=3, health_modifier=20)
    bread = Common("Slice of Bread", price=3, weight=2, health_modifier=20)

    inventory = [cup_of_beer, cheese, bread]

    cup_of_beer.report()