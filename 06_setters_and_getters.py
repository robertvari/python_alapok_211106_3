import random


class Dice:
    def __init__(self, color, sides):
        self._color = color
        self._sides = sides

        self.current_side = 1

    def roll(self):
        self.current_side = random.randint(1, self._sides)

    # setter method for color
    def set_color(self, new_color):
        allowed_colors = ["red", "green", "blue"]

        assert new_color in allowed_colors, f"The color must be {allowed_colors}"
        self._color = new_color

    def get_color(self):
        return self._color

    # setter method for sides
    def set_sides(self, new_sides):
        assert isinstance(new_sides, int), "side must be of type int"

        self._sides = new_sides

    def get_sides(self):
        return self._sides

    def report(self):
        print(f"Color: {self._color}")
        print(f"Sides: {self._sides}")

    def __str__(self):
        return f"Color: {self._color} Sides: {self._sides}"


my_dice = Dice("white", 6)
my_dice.set_color("red")
print(my_dice.get_color())

my_dice.roll()
print(my_dice.current_side)