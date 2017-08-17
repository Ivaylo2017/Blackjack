
'''
This method starts the game. It asks player for his/her name and then displays welcome message
It also performs all rules and conditions processing
The dealer deals 2 cards to the player and 2 to himself with only one of them visible in the beginning
Based on the value of the cards in her hand and the open card in the dealer's hand the player has t decide should she "hit"
another card or "stay". The goal is to score more than the dealer but less than 21. Whoever passes 21 "busts". 
The rules require the dealer to stop drawing cards when his score reaches 17. The Ace could be worth either 1 or 11.
'''
from card import Card
from deck import Deck
from player import Player
from account import Account
from blackjack import Blackjack

def main():

	playerName = input("Please enter a player name: ")
	newPlayer = Player(playerName)
	dealer = Player("Dealer")
	bjo = Blackjack(playerName)
	gameDeck = Deck()
	bjo.welcome_message()
	msg = ""
	while msg != 'n':
		print("Account: {}".format(newPlayer.account.start))
		bjo.player.reset_hand()
		bjo.dealer.reset_hand()
		newPlayer.account.bet = newPlayer.account.bet_eval()
		for i in range(2):
			bjo.deal_card(bjo.player)
			bjo.deal_card(bjo.dealer)
		bjo.display_cards()
		#If player has 21 from first 2 cards it's a blackjack and she immediately wins
		if bjo.player.calculate_hand() == 21:
			print("\nBLACKJACK!")
			newPlayer.win_blackjack()
			newPlayer.account.update_start()
		else:
			#Ask player if she wants another card 
			stayVariable = False
			while bjo.player.calculate_hand() < 21 and stayVariable == False:
				playerChoice = bjo.ask_player_decision()
				if playerChoice:
					bjo.deal_card(bjo.player)
					bjo.display_cards()
				else:
					stayVariable = True
			if bjo.player.calculate_hand() > 21:
				#Check to see if she's busted
				print("\nYou have busted!!! Try Again next time!")
				newPlayer.account.bet_lose()
				newPlayer.account.update_start()
			else:
				#When the player is done drawing cards fall in this condition and display both of dealer's cards
				bjo.display_cards("Final")
				dealerResult = bjo.dealer_plays()
				#Check different possible cases for dealer's score
				if  dealerResult == bjo.player.calculate_hand():
					bjo.display_cards("Final")
					print("\nTIE! You don't win or lose anything")
				elif dealerResult > bjo.player.calculate_hand() and dealerResult <= 21:
					bjo.display_cards("Final")
					print("\nYOU LOSE")
					newPlayer.account.bet_lose()
					newPlayer.account.update_start()
				elif dealerResult < bjo.player.calculate_hand() or dealerResult > 21:
					print("\nYOU WIN")
					newPlayer.account.bet_win()
					newPlayer.account.update_start()
		msg = input("Do you want to play another hand: ?")
	print("Thank you for playing 'Blackjack'! Exiting....")

if __name__ == "__main__":
	main()