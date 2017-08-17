import copy
from card import Card
from deck import Deck
from account import Account

#Define the Player class with attributes name, hand and account
class Player():

	def __init__(self, name):
		deck = Deck()
		card = Deck().deal()
		self.name = name
		self.hand = self.reset_hand()
		self.account = Account()
		#self.bet = self.account.bet()

	def reset_hand(self):
		self.hand = []
		return self.hand

	'''
	The claculate_hand() helps calculate the player's hand by assigning value of 10 to non-numeral card ranks
	If there's an Ace give it value of 11 unless the score goes beyond 21. In that case make it equal to 1
	Because we want to print the ranks of the cards and not the values we want to preserve the original 
	card attributes by creating a copy of it
	'''
	def calculate_hand(self):
		pic_rank = ['J','Q','K']
		sum = 0
		for card in self.hand:
			c = copy.copy(card)
			if c.rank in pic_rank: 
				c.rank = 10
			elif c.rank == 'A':
				if sum > 21:
					c.rank = 1
				else:
					c.rank = 11
			sum += int(c.rank)
			if sum > 21 and card.rank == 'A':
				sum -= 10
		return sum

	#This specially defined dundr str allows for friendly output of player hand
	def __str__(self):
		print("{}: {}".format(self.name, self.hand))