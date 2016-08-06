# Blackjack

class Player(object):
	def __init__(self, bank= 100):
		self.bank = bank
		
	def add_bank(self, amount):
		return self.bank += amount
		
	def lose_bank(self, amount):
		return self.bank -= amount
		
	