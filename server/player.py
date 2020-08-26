#This is going to define a player object on the server side
from .game import Game

class Player():
	def __init__(self, ip, name, game):
		self.game = None
		self.name = name
		self.ip = ip
		self.score = 0

	def set_game(self, game):
		self.game = game

	def update_score(self, x):
		self.score += x

	def guess(self, wrd):
		return self.game.player_guess(self,wrd)

	def disconnect(self):
		pass

	def get_score(self):
		return self.score

	def get_name(self):
		return self.name

	def get_ip(self):
		return self.ip
		