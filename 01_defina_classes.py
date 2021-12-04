# define a class
class Dice:
    # attribute of a class
    color = "white"
    sides = 6


class Person:
    name = "Robert"
    email = "robert@gmail.com"
    address = "Budapest"


# create an instance of a class
my_dice = Dice()
print(my_dice.color)
print(my_dice.sides)


robert = Person()
print(robert.name)
print(robert.address)
print(robert.email)