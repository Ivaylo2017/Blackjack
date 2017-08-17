'''
Class for managing the player's account 
'''
class Account(): 

	def __init__(self):
		self.start = 100
		self.amount = 0
		self.bet = 0

	#This method allows player to make bets as long as they have enough money in their account
	def bet_eval(self):
		flag = False
		self.bet = 0
		while not flag:
			n = int(input("Bet: "))
			if n <= self.start:
				self.bet = int(n)
				flag = True 
			else:
				print("You don't have sufficient funds. Please select smaller amount!")
		return self.bet

	def bet_win(self):
		self.amount = 2 * self.bet
		return self.amount

	def bet_lose(self):
		self.amount = 0
		return self.amount

	def win_blackjack(self):
		self.amount = 2.5*self.bet
		return self.amount

	def update_start(self):
		self.start -= self.bet
		self.start += self.amount
		if self.start < 1:
			print("You're left with",self.start,"money. Press Enter to proceed!")
			input()
			quit()
		else:
			print("Account: ", self.start)
			return self.start