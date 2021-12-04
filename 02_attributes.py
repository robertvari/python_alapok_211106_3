class Dice:
    # static attribute of a class
    color = "white"
    sides = 6


# instance
my_dice = Dice()
print(my_dice.color)
print(my_dice.sides)

# change dice color
my_dice.color = "red"

# print the instance attribute
print(my_dice.color)

# print the static attribute
print(Dice.color)