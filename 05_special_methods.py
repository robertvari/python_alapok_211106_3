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

    def __str__(self):
        return f"This is a {self.color} dice of {self.sides} sides."

    def __repr__(self):
        return f"Color: {self.color} Sides: {self.sides}"


my_dice1 = Dice("White", 6)
print(my_dice1)

my_dice2 = Dice("Blue", 10)
my_dice3 = Dice("Red", 8)
my_dice4 = Dice("Green", 20)

my_dice_collection = [my_dice1, my_dice2, my_dice3, my_dice4]
print(my_dice_collection)
