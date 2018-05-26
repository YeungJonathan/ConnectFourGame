from connect4_board import Board
from connect4_player import Player
import random

class Driver:

	def __init__(self):
		self.p1 = Player(1,'X')
		self.p2 = Player(2, 'O')
		self.board = Board()
	
	def prompt(self):
		userInput = int(input('Please input column to insert: '))
		return userInput
		
	def decideStart(self):
		#player 1 start if random integer is even
		#player 2 if odd
		if (random.randint(0,9) % 2 == 0): 
			print('Player 1 Start!')
			return self.p1, self.p2
		else:
			print('Player 2 Start!')
			return self.p2, self.p1
		
	def tick(self):
		starter, second = self.decideStart()
		while True:
			userinput = self.prompt()
			self.board.insert(userinput, starter)
			if self.board.win():
				return
			
			userinput = self.prompt()
			self.board.insert(userinput, second)
			if self.board.win():
				return
				
if __name__ == '__main__':
	main = Driver()
	main.tick()