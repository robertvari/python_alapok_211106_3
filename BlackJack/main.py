from game_assets.assets import AIPlayer, Player, Deck


class Blackjack:
    def __init__(self):
        self._intro()
        self.player_list = []

        self.create_players()

    def start_game(self):
        deck = Deck().create()
        bet = 0

        for player in self.player_list:
            bet += player.give_bet(10)
            player.draw_card(deck)

        # decide who won the round
        # give the bet to the winner

        # if player has credits
        #    ask of he/she want to play
        # else
        #   self.exit_game()
        pass

    def create_players(self):
        # create AI players
        for _ in range(3):
            new_AI_player = AIPlayer().create()
            self.player_list.append(new_AI_player)

        # create player
        new_player = Player().create()
        self.player_list.append(new_player)

        self.start_game()

    @staticmethod
    def exit_game():
        print("Thank you for playing my game. Have a nice day! :)")
        exit()
        pass

    @staticmethod
    def _intro():
        print("*"*50, "Blackjack", "*"*50)


if __name__ == '__main__':
    Blackjack()