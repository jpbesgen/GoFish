from controller import *


def testRemoveCardFromHand():

	ace_spades = Card(14, "spades")
	ace_hearts = Card(14, "hearts")
	jack_diamonds = Card(11, "diamonds")
	king_hearts = Card(13, "hearts")

	cardList = [ace_spades, ace_hearts, jack_diamonds, king_hearts]
	print(cardList)
	cardList.remove(ace_hearts)
	print(cardList)

def testPlayerCheckForPairs():
	ace_spades = Card(14, "spades")
	ace_hearts = Card(14, "hearts")
	jack_diamonds = Card(11, "diamonds")
	king_hearts = Card(13, "hearts")
	seven_clubs = Card(7, "clubs")
	seven_spades = Card(7, "spades")
	seven_hearts = Card(7, "hearts")
	six_spades = Card(6, "spades")
	six_hearts = Card(6, "hearts")
	six_diamonds = Card(6, "diamonds")
	six_clubs = Card(6, "clubs")


	cardList = [ace_spades, ace_hearts, jack_diamonds, king_hearts, 
		seven_clubs, seven_spades, seven_hearts, 
		six_clubs, six_spades, six_hearts, six_diamonds]

	p1 = Player(1, "Jack", cardList)

	print("list before check pairs")
	print(cardList)
	p1.checkForPairs()
	print("list after check pairs")
	print(cardList)
	print("pairs")
	print(p1.pairs)

def testCardEquivalence():

	card1 = Card(1, "spades")
	card2 = Card(2, "spades")
	card3 = Card(1, "hearts")

	print("card1 == card2:")
	print(card1 == card2)
	print("card1 num: {}, card2 num: {}".format(card1.number, card2.number))

	print("card2 == card3:")
	print("card1 num: {}, card3 num: {}".format(card1.number, card3.number))
	print(card1 == card3)

	list1 = [card2]
	list2 = [card1, card2]
	print("card3 in list1: {}".format(card3 in list1))
	print("card3 in list2: {}".format(card3 in list2))

def testDeck():
	deck = Deck()
	print(deck.deck)

def testHands():

	p1 = Player(1, "p1")
	p2 = Player(2, "p2")
	players = [p1, p2]

	gameDeck = Deck()
	p1.addToHand(gameDeck)
	print("player 1 hand")
	print([hand for hand in p1.hand])
	print("player 1 pairs")
	print([pair for pair in p1.pairs])

	p2.addToHand(gameDeck)
	print("player 2 hand")
	print([hand for hand in p2.hand])
	print("player 2 pairs")
	print([pair for pair in p2.pairs])
