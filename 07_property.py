class Dice:
    def __init__(self, color, sides):
        # instance attributes
        self._color = color
        self._sides = sides

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, new_sides):
        self._sides = new_sides


my_dice = Dice("White", 6)
print(my_dice.color)
print(my_dice.sides)

my_dice.color = "Red"
my_dice.sides = 10