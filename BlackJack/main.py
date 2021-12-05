class Blackjack:
    def __init__(self):
        self._intro()
        self.player_list = []

        self.create_players()

    def start_game(self):
        # create deck
        # store bet = 0

        # for player in player_list
           # ...

        # decide who won the round
        # give the bet to the winner

        # if player has credits
        #    ask of he/she want to play
        # else
        #   self.exit_game()
        pass

    def create_players(self):
        # create AI players
        # create player

        # self.start_game()
        pass

    def exit_game(self):
        print("Thank you for playing my game. Have a nice day! :)")
        exit()
        pass

    def _intro(self):
        print("*"*50, "Blackjack", "*"*50)


if __name__ == '__main__':
    Blackjack()