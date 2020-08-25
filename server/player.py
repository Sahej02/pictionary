#This is going to define a player object on the server side

class Player():
	def __init__(self, ip, name):
		self.name = name
		self.ip = ip
		self.score = 0

	def update_score(self, x):
		self.score += x

	def guess(self, string):
		pass

	def disconnect(self):
		pass

	def get_score(self):
		return self.score

	def get_name(self):
		return self.name

	def get_ip(self):
		return self.ip
		