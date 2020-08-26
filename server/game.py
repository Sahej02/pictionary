from .player import Player
from .round import Round
from .board import Board
import random

class Game(object):
    def __init__(self, id, players):
        self.id = id
        self.players = []
        self.words_used = []
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0

    def start_new_round(self):
        self.round = Round(self.get_word(), self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.round_ended()
            self.end_game()     

    def player_guess(self, player, guess):
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        pass

    def skip(self):
        if self.round:
            check = self.round.skip()
            if check:
                self.round_ended()

        else:
            raise Exception("Round not started yet")

    def round_ended(self):
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):
        if not self.board:
            raise Exception("No board yet")
        self.board.update(x,y,color)
    
    def end_game(self):
        pass

    @staticmethod
    def get_word():
        with open("words.txt", "r") as f:
            words = f.readlines()
            i = random.randint(0, len(words))
            return words[i].strip()
