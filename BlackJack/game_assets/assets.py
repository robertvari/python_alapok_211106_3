import random


class PlayerBase:
    name_list = ["Brittney Moriah", "Curtis Tristin", "Lucas Troy", "Chip Gale", "Simon Lynn"]

    def __init__(self):
        self._name = None
        self._credits = 0
        self._hand = []
        self._in_game = True

    def create(self):
        self._credits = random.randint(100, 1000)
        self._name = random.choice(PlayerBase.name_list)

    def report(self):
        print(f"Name: {self._name}")
        print(f"Credits: {self._credits}")
        print(f"Cards in hand: {self._hand}")

    def draw_card(self, deck):
        while self._in_game:
            hand_value = self.count_hand()

            if hand_value > 16:
                self._in_game = False

                if hand_value > 21:
                    print(f"{self._name} lost his turn.")
                else:
                    print(f"{self._name} passes.")
            else:
                new_card = deck.give_card()
                self._hand.append(new_card)

    def count_hand(self):
        return sum([card.value for card in self._hand])

    def show_hand(self):
        print(f"Cards in hand: {self._hand}")


class Player(PlayerBase):
    def create(self):
        super(Player, self).create()

        self._name = input("What is your name?")


class AIPlayer(PlayerBase):
    pass


class Card:
    def __init__(self, name: str, value: int):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __repr__(self):
        return f"{self._name} {self._value}"


class Deck:
    def __init__(self):
        self._cards = []

    def create(self):
        self._cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card in cards:
                card_name = f"{name} {card[0]}"
                card = Card(card_name, card[1])
                self._cards.append(card)

        random.shuffle(self._cards)

    def give_card(self):
        new_card = self._cards[-1]
        self._cards.remove(new_card)
        return new_card

    def __str__(self):
        return f"{self._cards}"


if __name__ == '__main__':
    deck = Deck()
    deck.create()

    ai_player = AIPlayer()
    ai_player.create()

    ai_player.draw_card(deck)
    ai_player.show_hand()
    print(ai_player.count_hand())