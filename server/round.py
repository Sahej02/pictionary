#represents a round of the game, stores word, time, skips etc
import time
from _thread import start_new_thread
from .game import Game
from .chat import Chat


class Round():
	def __init__(self, word, player_drawing, players):
		self.word = word
		self.player_drawing = player_drawing
		self.player_guessed = []
		self.skips = 0
		self.player_scores = {player:0 for player in players}
		self.time_var = 75
		self.chat = Chat(self)
		start_new_thread(self.time_thread, ())

	def skip(self):
		self.skips += 1
		if self.skips > len(self.player_scores) - 2:
			return True
		
		return False

	def time_thread(self):
		while self.time_var > 0:
			time.sleep(1000)
			self.time_var -= 1
		self.end_round("Time is up")

	def guess(self, player, word):
		correct =  word == self.word
		if correct:
			self.player_guessed.append(player)

	def player_left(self, player):
		if player in self.player_scores:
			del self.player_scores[player]

		if player in self.player_guessed:
			self.player_guessed.remove(player)

		if player == self.player_drawing:
			self.end_round("Player who was drawing left")

	def end_round(self, msg):
		pass
