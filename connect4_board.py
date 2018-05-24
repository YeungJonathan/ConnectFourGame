import copy

class Board:

	def __init__(self, row = 6, column = 7):
		self.board = [['.' for x in range(column)]for y in range(row)]
		self.__row = row
		self.__column = column
		
	def printPretty(self):
		for item in self.board:
			for position in item:
				print(position, end=" ")
			print("")
	
	def getRow(self):
		return copy.deepcopy(self.__row)
		
	def getColumn(self):
		return copy.deepcopy(self.__column)
	
	def insert(self, insert_column, player):
		for i in range(self.getRow()-1, -1, -1):
			if self.board[i][insert_column] == '.':
				self.board[i][insert_column] = player.getSymbol()
				return
		
