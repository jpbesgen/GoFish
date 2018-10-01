from tests import *
from classes import *
from utils import *

"""
This file contains the Game class, which provides the game state.
"""

class Game():
	""" Class to create an instance of a game of Go-Fish. """

	def __init__(self):
		"""Create a game state with NUMPLAYERS, GAMEDECK, and list of PLAYERS.

		numPlayers -- number of players in the game.
		gameDeck -- Deck of cards to be used for the current game state.
		players -- list of players in the game.
		"""
		self.numPlayers = 0
		self.gameDeck = Deck()
		self.players = []

	def guessPlayerAndCard(self, currentPlayer):
		""" Ask current player for opposing player number to guess card from. """
		ask = inputPlayerNumber(self.numPlayers, self.players)
		print("")

		if ask == currentPlayer.number:
			print("You can't ask yourself! Pick another number \n")
			self.guessPlayerAndCard(currentPlayer)
			return
		otherPlayer = self.players[ask-1]
		self.askForPair(currentPlayer, otherPlayer)

	def askForPair(self, currentPlayer, otherPlayer):
		""" Ask current player for card to guess from opposing player's hand. """
		printHand(currentPlayer)
		printPairs(currentPlayer)
		guess = inputGuess()
		print("")

		if not currentPlayer.hasCard(guess):
			print("You can only ask for a card in your hand!\n")
			self.askForPair(currentPlayer, otherPlayer)
			return
		if otherPlayer.hasCard(guess):
			self.matchGuess(currentPlayer, otherPlayer, guess)
			print("It's a match.")
			if currentPlayer.hasCards():
				print("You get another guess! \n")
				self.guessPlayerAndCard(currentPlayer)
				return
			elif self.gameDeck.isEmpty():
				print("You are out of cards and the deck is empty! Wait for other players to finish their turns.")
				return
		else:
			print("No match! Go Fish! \n")
			currentPlayer.goFish(self.gameDeck)
			holdOutput(2)

	def matchGuess(self, currentPlayer, otherPlayer, guess):
		""" Check if current player's guess matches any cards in the opposing player's hand. """
		card = Card(guess, "")
		card = otherPlayer.removeFromHand(card)
		currentPlayer.matchGuess(card, self.gameDeck)
		otherPlayer.drawCard(self.gameDeck)

	def checkCardsInHand(self, player):
		""" Ensure that the player has 5 cards in their hand. """
		if player.numCardsInHand() < 5 and not self.gameDeck.isEmpty():
			player.drawCard(self.gameDeck)
			self.checkCardsInHand(player)
		return

	def startGame(self):
		""" Set-up the game, creating the players and adding 5 cards to each of their hands. """
		self.numPlayers = inputNumPlayers()

		for i in range(self.numPlayers):
			name = inputName(i+1)
			self.players.append(Player(i+1, name))

		for _ in range(5):
			for player in self.players:
				player.drawCard(self.gameDeck)

	def play(self):
		""" Loop while game is not over. """
		self.startGame()
		currentPlayer = 0

		while any([p.hasCards() for p in self.players]):
			clear()
			player = self.players[currentPlayer]
			print("Hi {}! You are player {}.".format(player.name, player.number))
			if player.hasCards():
				self.checkCardsInHand(player)
				self.guessPlayerAndCard(player)
			currentPlayer += 1
			currentPlayer = currentPlayer % self.numPlayers

		print("\nThe game is over!\n")
		printHandsAndPairs(self.players)
		totalPairs = [len(p.pairs) for p in self.players]
		winnerIndex = totalPairs.index(max(totalPairs))
		print("\nPlayer {} wins with {} pairs!".format(winnerIndex+1, totalPairs[winnerIndex]))


