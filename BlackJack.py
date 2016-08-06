# Blackjack
import random

"""
Class for player. 
"""
class Player(object):
	def __init__(self, bank= 100):
		self.bank = bank
		
	def add_bank(self, amount):
		return self.bank += amount
		
	def lose_bank(self, amount):
		return self.bank -= amount
		
"""
Dealer class inehrits from Player class
"""
class Dealer(Player):
	def __init__(self, bank=1000):
		self.bank = bank
		
		
"""
Card class to initialize types of cards
"""
class Card(object):

	# Class attributes
	suit_name = ("Clubs", "Spades", "Diamonds", "Hearts")
	rank_name = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9",
						"10", "Jack", "Queen", "King")
						
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		
	def __str__(self):
		return self.suit + self.rank
		
	def get_rank(self):
		return self.rank
	
	def get_suit(self):
		return self.suit
		
	def draw(self):
		print(self.suit + self.rank)
		
