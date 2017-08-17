import random
from card import Card
#Define the Deck Class
class Deck():
	
	def __init__(self):
		self.rank = [str(i) for i in range(2,11)] + ['J','Q','K','A']    # List concat to create a list of all possible card ranks. Ace is 1 point
		self.suit = ["Spades","Hearts","Diamonds","Clubs"]
		self.deck = self.start()
		#self.card = Card()

	#Create new shuffled full deck consisting of 1 set of 52 crads
	def start(self):
		new_deck = []
		for r in self.rank:
			for s in self.suit:
				new_card = Card(r,s)
				new_deck.append(new_card)
		random.shuffle(new_deck)
		return new_deck

	'''
	Return random card from the deck any time this method is called.  
	The card is also removed from the deck so it doesn't come up again. Technically card should come from the top
	of the deck so shuffle() and pop(0) could be used instead in writing this method. For our purposes here this is
	insignificant.
	'''
	def deal(self):
		new_deal = random.choice(self.deck)
		self.deck.remove(new_deal)
		if len(self.deck) < 4:
			#If less then 4 cards are left in deck we call the start() method an basically shuffle all the cards back in
			print("There are less than {} cards left in deck. Reshuffling...".format(len(self.deck)))
			self.deck = self.start()
		return new_deal