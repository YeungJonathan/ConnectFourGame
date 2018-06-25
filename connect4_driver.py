from connect4_board import Board
from connect4_board import Player
import random

class Driver:

	def __init__(self):
		self.p1 = Player(1,'X')
		self.p2 = Player(2, 'O')
		self.board = Board()
	
	def prompt(self):
		userInput = -1
		while userInput < 0 or userInput > 6:
			userInput = int(input('Please input column to insert (0-6): '))
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
		print(self.board)
		while True:
			userinput = self.prompt()
			row = self.board.findRow(userinput, starter)
			starter.addMoves(row, userinput)
			print(self.board)
			if starter.checkWin():
				print('P1 Won')
				return
			
			userinput = self.prompt()
			row = self.board.findRow(userinput, second)
			second.addMoves(row, userinput)
			print(self.board)
			if second.checkWin():
				print('P2 Won')
				return


if __name__ == '__main__':
	main = Driver()
	main.tick()