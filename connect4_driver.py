from connect4_board import Board
from connect4_board import Player
import random

class Driver:

	def __init__(self):
		playerOne = input('Input Player 1 name: ')
		playerTwo = input('Input Player 2 name: ')
		self.p1 = Player(1,'X', playerOne)
		self.p2 = Player(2,'O', playerTwo)
		self.board = Board()
	
	def prompt(self, name):				
		while True:
			try:
				userInput = int(input(name+' Insert Column (1-7): '))
				if not (1 <= userInput <= 7):
					raise ValueError
				if self.board.board[0][userInput-1]!='.':
					raise Exception
			except ValueError:
				print('Please enter an integer from 0-7')
				continue
			except Exception:
				print('Column reached maximum. ',end = '')
				continue		
			return userInput-1
		
	def decideStart(self):
		#player 1 start if random integer is even
		#player 2 if odd
		if (random.randint(0,9) % 2 == 0): 
			print(self.p1.getPlayerName(),'Start!')
			return self.p1, self.p2
		else:
			print(self.p2.getPlayerName(),'Start!')
			return self.p2, self.p1
			
	def printBoard(self):
		print(self.board, end = '')
		print('-------------')
		print('1 2 3 4 5 6 7')
		
	def playerInsert(self, player):
		'''
		Method to insert player moves
		Method to change update the board
		'''
		userinput = self.prompt(player.getPlayerName())
		row = self.board.findRow(userinput, player)
		player.addMoves(row, userinput)
		self.printBoard()
		if player.checkWin():
			print(player.getPlayerName(),'Won')
			return True
		return False

	
	def tick(self):
		starter, second = self.decideStart()
		endGame = False
		self.printBoard()
		while not endGame:
			#starter insert
			endGame = self.playerInsert(starter) or self.board.isFull()
			if endGame is True:
				break 		
			#second insert
			endGame = self.playerInsert(second) or self.board.isFull()
		if self.board.isFull():
			print('The game is tied!')

if __name__ == '__main__':
	main = Driver()
	main.tick()