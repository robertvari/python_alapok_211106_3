from game_assets.assets import AIPlayer, Player, Deck


class Blackjack:
    def __init__(self):
        self._intro()
        self.player_list = []
        self.bet = 0

        self.create_players()

    def start_game(self):
        deck = Deck().create()
        self.bet = 0

        for player in self.player_list:
            player.reset_player()

            self.bet += player.give_bet(10)
            player.draw_card(deck)

        # decide who won the round
        self._get_winner()

    def _get_winner(self):
        player_list = [player for player in self.player_list if player.count_hand() <= 21]

        if player_list:
            winner_list = sorted(player_list, key=lambda p: p.count_hand())
            winner = winner_list[-1]

            print(f"The winner: {winner} who wins {self.bet} credits.")
            winner.add_credits(self.bet)
        else:
            print("House wins.")

        player = self.player_list[-1]
        if player.has_credits:
            print(f"You have {player.credits}")

            result = input("Do you want to play again? (y/n)")
            if result == "y":
                self.start_game()
            else:
                self.exit_game()
        else:
            self.exit_game()

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