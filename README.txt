
Joseph Besgen

Go-Fish card game for the KPCB Fellowship application.


Instructions to run game:
Note: this was only tested with Python3 on a Mac, so performance on a PC or Linux machine or with Python2 is not guaranteed.

In terminal or at the command line, run:
python3 main.py

Tests (though not thorough/complete), can be run using:
python3 tests.py


Game Play:

	To exit at anytime, type "Exit" or "exit".

	Start: 
	At start, the game will prompt you to enter the number of players and then each players name. Type this information and press enter. 

	Each player has a "hand" and a "pairs" list. These lists correspond to the current cards in the player's hand and the pairs the player has already gotten, respectively.

	Rules:

	- The object of the game is to end with as many pairs as possible.
	- Each player starts with 5 cards. 
		- If any of the cards in the starting hand form a pair, that pair gets put into the player's "pairs" list.
	- Each turn, the current player tries to match one of their cards with one of their opponent's (based on card number, not suit).

	- On each turn:
		- The current player will be asked which player they want to "guess" a card from. Once a player is picked (which cannot be the current player themself), the current player is asked to pick a card from their hand. If the chosen opposing player has a card that matches the guessed number, both cards get taken out of their respective hands and get put into the current player's pairs list.

		- When a player gives up a card that another player guessed, that player then automatically draws another card from the deck. If this new card matches any of the cards in the player's hand, the match will be placed into their pairs list and they will draw again until they have 5 cards and no matches in their hand. 
			- It may appear that a player "magically" gains pairs of cards. This is due to this fact.

		- If the current player correctly guesses the opponents card and matches a pair, they get to guess again until they make an incorrect guess, in which case "Go Fish" is displayed and they draw a new card.

	- At the end of the game, the player with the most number of pairs wins.


Design Choices:

I separated the game into four main files: classes.py, utils.py, controller.py, and main.py. I also included a tests.py file that includes methods which had print statements for unit testing. With more time, I would have written more comprehensive unit tests and used Python's built in unit testing.

"classes.py":
	 - This file contains the classes for Player, Card, and Deck. These were the minimul classes needed to play the game. 
	 - Player:
	 	- Each player has two lists: a "hand" and a "pairs" list, both of which contain cards.
	 	- Contains methods to add and remove cards from hand and pairs lists.
	 - Card:
	 	- A card has a number and a suit.
	 - Deck:
	 	- A deck contains a list of all 52 cards that would be found in a standard deck of cards. 
	 	- The deck acts as a queue and can "pop" cards from the front, simulating "drawing a card"

"controller.py":
	- This file contains the Game class, which is used to create the current game state. The class has methods that are called when the game is played. 

"utils.py":
	- This file contains helper methods for the program, mainly print and input functions.

"main.py":
	- This file simply runs the game.

External Libraries:
- Random for the shuffle function
- os for the ability to clear and sleep terminal output

Choice of tooling:
- I used Python mainly because it is one of my preferred languages and is easy to set-up and call via the command line.
