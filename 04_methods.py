import random

class Dice:
    # static attribute
    number_of_dices_created = 0

    def __init__(self, color, sides):
        # instance attributes
        self.color = color
        self.sides = sides
        self.current_side = 1

        Dice.number_of_dices_created += 1

    # class method
    def report(self):
        print(f"Color: {self.color}")
        print(f"Sides: {self.sides}")

    def roll(self):
        # store new current_side
        self.current_side = random.randint(1, self.sides)


my_dice = Dice("White", 6)
for i in range(10):
    my_dice.roll()

print(my_dice.current_side)


my_dice2 = Dice("Blue", 10)
for i in range(10):
    my_dice2.roll()

print(my_dice2.current_side)