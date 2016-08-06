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
	card_val = {"Ace": 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
						'7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
							'Queen': 10, 'King': 10}
						
	def __init__(self, rank, suits):
		self.rank = rank
		self.suits = suits
		
	def __str__(self):
		return self.suits + self.rank
		
	def get_rank(self):
		return self.rank
	
	def get_suit(self):
		return self.suits
		
	def draw(self):
		print(self.suits + self.rank)
		
"""
Deck class 
"""
class Deck(object):

	# Initialize a deck of all the cards
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranking
				self.deck.append(Card(suits, rank)
				
	# Method to shuffle deck
	def shuffle(self):
		random.shuffle(self.deck)
	
	# Deal out one card at a time
	def deal(self):
		dealt_card = self.deck.pop()
		return dealt_card
		
class Hand(object):
	def __init__(self):
		self.cards = []
		self.value = 0
		self.ace = False
		
	def __str__(self):
		curr_hand = ""
		
		for card in self.cards:
			name = card.__str__()
			curr_hand += " " + name
			
		return 'You currently have: %s' %curr_hand
		
	# Add a card to your hand
	def add_card(self, card):
		self.cards.append(card)
		
		# Check if one of the cards is an Ace
		if card.rank == 'Ace':
			self.ace = True
			
		self.value += card_val[card.rank]
		
	# Return the value of your hand
	def card_value(self):
		# Have an ace and total hand is less than 12
		if(self.ace == True and self.value < 12):
			return self.value + 10
		else:
			return self.value
				
			
