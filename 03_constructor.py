class Dice:
    # static attribute
    number_of_dices_created = 0

    def __init__(self, color, sides):
        # instance attributes
        self.color = color
        self.sides = sides

        Dice.number_of_dices_created += 1


my_dice1 = Dice("white", 6)
print(f"my_dice1 color: {my_dice1.color}")
print(f"my_dice1 sides: {my_dice1.sides}")


my_dice2 = Dice("red", 10)
print(f"my_dice2 color: {my_dice2.color}")
print(f"my_dice2 sides: {my_dice2.sides}")


my_dice3 = Dice("blue", 20)
print(f"my_dice3 color: {my_dice3.color}")
print(f"my_dice3 sides: {my_dice3.sides}")


print(f"Number of dices created: {Dice.number_of_dices_created}")