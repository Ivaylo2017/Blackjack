#Define the Card class
class Card():
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		"{} of {}".format(self.rank, self.suit)