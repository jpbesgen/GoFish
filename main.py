from controller import *
from utils import printWelcome

def main():

	printWelcome()

	game = Game()
	game.play()


if __name__ == '__main__':
	main()