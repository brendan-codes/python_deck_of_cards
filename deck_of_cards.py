from random import shuffle
import pprint

class Deck(object):
	def __init__(self):
		self.deck = []
		self.reset()
		self.shuffle()

	def reset(self):
		self.deck = []

		suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
		pips = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

		for suit in range(0, len(suits)):
			for pip in range(0, len(pips)):
				self.deck.append(pips[pip] + " of " + suits[suit])

		return self

	def shuffle(self):
		shuffle(self.deck)
		return self

	def deal(self):
		return self.deck.pop()

class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.deal())
		return self
		
	def discard():
		self.hand = []
		return self

class Card(object):
	def __init__(self, pip, suit):
		self.pip = pip
		self.suit = suit



deck3 = Deck()

deck3.shuffle().shuffle().reset().shuffle()

print deck3
# deck1 = Deck()
# deck3 = Deck()

# player1 = Player('Brendan')
# player1.draw(deck1).draw(deck1)
# pprint.pprint(deck1.deck);
# print player1.hand[0].pip
# print player1.hand[0].suit
# print player1.hand[1].pip
# print player1.hand[1].suit


# print deck1.deck