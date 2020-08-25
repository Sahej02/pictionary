#the chat box on the side

class Chat():
	def __init__(self):
		self.content = []

	def update_chat(self, msg):
		self.content.append(msg)

	def get_chat(self):
		return self.content

	def __len__(self):
		return len(self.content)

	def __str__(self):
		return " ".join(self.content)

	def __repr__(self):
		return str(self)