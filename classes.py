from random import shuffle
from utils import printMatchedCard


""" 
This file contains the main classes for the "Go-Fish" card game. 

""" 

class Player: 
	""" Player in the game."""

	def __init__(self, number, name):
		"""Create a Player with given NAME and NUMBER.

		hand -- A list of cards in the player's hand
		pairs -- A list of current pairs (tuples of 2 cards) that player has. 
		"""
		self.number = number
		self.name = name
		self.hand = []
		self.pairs = []


	def hasCard(self, cardAsked): 
		if Card(cardAsked, "") in self.hand:
			return True
		return False

	def hasCards(self):
		return not len(self.hand) == 0

	def numCardsInHand(self):
		return len(self.hand)

	def goFish(self, deck):
		self.drawCard(deck)

	def matchGuess(self, card, deck):
		"""Helper function for removeFromHand(), called when 
		If the number of cards in the hand decreases to zero, 
		"""
		matchingCard = self.removeFromHand(card)
		self.pairs.append((card, matchingCard))
		if len(self.hand) == 0:
			self.drawCard(deck)

	def addToHand(self, card, deck):
		""" If matching card is in hand, remove both, add to pairs list, and 
		draw a new card. Otherwise, add card to current hand.
		"""
		if card in self.hand:
			toRemove = self.hand[self.hand.index(card)]
			self.pairs.append((card, toRemove))
			self.hand.remove(toRemove)
			self.drawCard(deck)
			self.drawCard(deck)
			# Commenting out to reduce confusing during game play for new players.
			# This code just prints when a player draws a card that matches one in 
			# their hand.
			# if self.number in Card.faceCards:
			# 	printMatchedCard(self.name, Card.faceCards[self.number])
			# else:
			# 	printMatchedCard(self.name, card.number)
		else:
			self.hand.append(card)

	def drawCard(self, deck):
		""" Draw card from deck and add to hand. """
		if not deck.isEmpty():
			card = deck.pop()
			self.addToHand(card, deck)
		elif not deck.printedEmpty():
			print("The deck is empty. The last card has been drawn. ")

	def removeFromHand(self, card):
		""" Remove card from hand. """
		if card not in self.hand:
			raise RuntimeError("Card does not exist in hand; cannot remove.")
		else:
			toRemove = self.hand[self.hand.index(card)]
			self.hand.remove(card)
			return toRemove

class Card:
	""" Represents a playing card with a given number and suit. In the context
	of this game (Go-Fish), suits serve no purpose other than to distinguish cards 
	in the deck. 
	"""
	faceCards = {11: "jack", 12: "queen", 13: "king"}

	def __init__(self, number, suit):
		"""Create a playing card with given NUMBER and SUIT.

		number -- 1 through 13, where 11=Jack, 12=Queen, 13=King.
		suit -- A string; either clubs, spades, hearts, or diamonds.
		"""
		self.number = number
		self.suit = suit

	def __eq__(self, otherCard):
		"""Set card equivalence to be based on number, since suits are irrelevant in Go-Fish. """
		return self.number == otherCard.number

	def __str__(self):
		if self.number in Card.faceCards:
			return "{} of {}".format(Card.faceCards[self.number], self.suit)
		else:
			return "{} of {}".format(self.number, self.suit)
	def __repr__(self):
		if self.number in Card.faceCards:
			return "{} of {}".format(Card.faceCards[self.number], self.suit)
		else:
			return "{} of {}".format(self.number, self.suit)

class Deck: 
	""" A Deck represents a deck of cards. Each deck contains 52 cards. """
	def __init__(self):
		"""Create the deck for the game. 
		
		deck -- array containing all 52 cards
		empty -- boolean representing if the deck is empty
		"""
		self.deck = self.createDeck()
		self.empty = False
		self.shuffleDeck()

	def createDeck(self):
		""" Initialize deck with 52 cards, 1 from each number/facecard and suit combination."""
		deck = []
		for suit in ["clubs", "spades", "hearts", "diamonds"]:
			for num in range(1,14):
				deck.append(Card(num, suit))
		return deck
	
	def shuffleDeck(self):
		""" Shuffle deck using Python's random.shuffle. """
		shuffle(self.deck)

	def pop(self):
		""" Return the top card from the deck. """
		if not self.isEmpty():
			return self.deck.pop()
		return

	def isEmpty(self):
		if self.length() == 0:
			self.empty = True
			return True

	def length(self):
		return len(self.deck)

	def printedEmpty(self):
		return self.empty





	



