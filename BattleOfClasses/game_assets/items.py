class ItemBase:
    def __init__(self):
        self.price = 0
        self.weight = 0


class Common(ItemBase):
    # Item Base
    pass


class WeaponBase(ItemBase):
    # Item Base
    pass


class CommonWeapon(WeaponBase):
    # ItemBase, WeaponBase
    pass


class MagicWeapon(WeaponBase):
    # ItemBase, WeaponBase
    pass