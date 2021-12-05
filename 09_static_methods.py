class Dice:
    # static attribute
    count = 0

    def __init__(self):
        self._color = "white"
        self._sides = 6

    def roll(self):
        pass

    @staticmethod
    def print_hello():
        print("Hello, I'm a dice")


Dice.print_hello()
print(Dice.count)