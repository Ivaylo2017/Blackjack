from player import Player
from deck import Deck
from card import Card

#Blackjack is fundamentally a game between a player and the dealer. This class defines their interactions
class Blackjack():
	def __init__(self,player):
		self.player = Player(player)
		self.dealer = Player("Dealer")
		self.gameDeck = Deck()

	def welcome_message(self):
		#Printing welcome message
		print("""
			WELCOME TO BLACKJACK!!!
				by "Alex"

			  GOOD LUCK, {}!
				""".format(self.player.name))

	def deal_card(self,player):
		# Anytime this method is called , depending on the player who calls it will pop the top card
		if player.name == "Dealer":
			#from the deck with deal() method and will add it to player's hand 
			self.dealer.hand.append(self.gameDeck.deal())
		else:
			self.player.hand.append(self.gameDeck.deal())
	'''
	In displaying cards that each player has drawn we need to consider these rules:
	During the game player should be able to see all his cards. For the dealer only the second card should be shown (using for loop
	i show all the cards from index 1 till the end which is technically just the second card) and Unknown displayed for his other card
	Once the player has stopped drawing cards the dealer has to show his "Unknown" card and draw cards while his score is less than 17
	This method takes optional parameter which will allow us to display all of dealer's cards once the player is done drawing. To do that 
	we need to pass it the "Final" value to it.
	'''
	def display_cards(self, howto="",split=""):
		if howto =="Final":
			dealerString = " "
			for card in self.dealer.hand:
				dealerString += str(card.rank) + " "
			print("\nDealer Hand: ", dealerString)
			playerString =  " "
			for card in self.player.hand:
				playerString += str(card.rank) + " "
			print("{}'s Hand: ".format(self.player.name), playerString)
		else:
			dealerString = "? "
			for card in self.dealer.hand[1:]:
				dealerString += str(card.rank) + " "  #it could also be written without for loop dealerString += str(self.dealer.hand[1].rank) + " "
			print("\nDealer Hand: ", dealerString)

			playerString = " "
			for card in self.player.hand:
				playerString += str(card.rank) + " "
			print("{}'s Hand: ".format(self.player.name), playerString)		

	def ask_player_decision(self):
		#This method asks if the player wants to hit (i.e draw another card) or stay
		decision = ""
		while decision != "h" and decision != "s":
			decision = input('''\n\t\tWhat would you like to do? To hit, type "h". To stay, type "s"\n\t\t\t\t''')
		if decision == "h":
			return True
		else:
			return False

	def dealer_plays(self):
		#Here we set the condition for how long should dealer keep asking for a card
		while self.dealer.calculate_hand() < 17:
			print("\nDealer hits")
			self.deal_card(self.dealer)
			self.display_cards("Final")
		return self.dealer.calculate_hand()