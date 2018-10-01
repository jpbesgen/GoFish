from os import system, name 
from time import sleep 

"""
This file contains helper functions for the program, mainly print and input functions.
"""
  
def clear(): 
  
	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 

def holdOutput(time):
	sleep(time)

def inputNumPlayers():
	num = 0
	try:
		num = input("Please enter the number of players (2 - 5): ")
		checkExit(num)
		num = int(num)
	except ValueError:
		print("Please enter a valid integer 2 - 5")
		num = inputNumPlayers()
	if num < 2 or num > 5:
		print("Please enter a valid integer 2 - 5")
		num = inputNumPlayers()
	return num

def inputName(playerNum):
	name = ""
	try:
		name = input("Please enter player {}'s name: ".format(playerNum))
		checkExit(name)
	except ValueError:
		print("Please enter a valid string")
		name = inputName(playerNum)
	return name

def inputPlayerNumber(numPlayers, players):
	num = 0
	try:
		num = input("Please enter the number of the player you would like to ask (1 - {}): ".format(numPlayers))
		checkExit(num)
		num = int(num)
	except ValueError: 
		print("Please enter a valid integer 1 - {} ".format(numPlayers))
		num = inputPlayerNumber(numPlayers, players)
	if num < 1 or num > numPlayers:
		print("Please enter a valid integer 1 - {} ".format(numPlayers))
		num = inputPlayerNumber(numPlayers, players)
	if not players[num-1].hasCards():
		print("Player {} is out of cards. Please choose another player".format(num))
		num = inputPlayerNumber(numPlayers, players)
	return num

def inputGuess():
	guess = 0
	try:
		print("\nPlease enter the number of your guess")
		guess = input("(1-10 or 11 for jack, 12 for queen, 13 for king): ")
		checkExit(guess)
		guess = int(guess)
	except ValueError:
		print("Please enter a valid integer. ")
		guess = inputGuess()
		return
	if guess <= 0 or guess > 13:
		print("Please enter a valid integer 1-13")
		guess = inputGuess()
	return guess

def checkExit(exit):
	if exit == "exit" or exit == "Exit":
		raise SystemExit

def printMatchedCard(playerName, cardNum):
	faceCards = {11: "jack", 12: "queen", 13: "king"}
	if cardNum in faceCards:
		print("{} matched a pair of {}s when drawing a card. \n".format(playerName, faceCards[cardNum]))
	else:
		print("{} matched a pair of {}s when drawing a card. \n".format(playerName, cardNum))


def printHandsAndPairs(players):
	i = 0
	for player in players:
		print("player {} pairs".format(i+1))
		print([pair for pair in players[i].pairs])
		i += 1

def printHand(currentPlayer):
	print ("Here are the cards in your hand: \n{}".format(currentPlayer.hand))

def printPairs(currentPlayer):
	print("Here are your current pairs: \n{}".format(currentPlayer.pairs))

def printWelcome():
	print("\nThank you for playing Go Fish! \n" +
		"This game was made by Joseph Besgen for the KPCB Fellowship Application. \n" +
		"Please check the README to answer any questions about the game. \n"
		"Type \"exit\" at anytime to exit the game. \n")

