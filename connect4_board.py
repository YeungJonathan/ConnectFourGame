import copy


class Board:

	def __init__(self, row = 6, column = 7):
		self.board = [['.' for x in range(column)]for y in range(row)]
		self.__row = row
		self.__column = column

	def __str__(self):
		string = ""
		for item in self.board:
			for position in item:
				string += position
				string += ' '
			string += "\n"
		return string

	def insert(self, insert_column, player):
		for i in range(self.__row - 1, -1, -1):
			if self.board[i][insert_column] == '.':
				self.board[i][insert_column] = player.getSymbol()
				#				print(self.board)
				return
	
	def getRow(self):
		return copy.deepcopy(self.__row)
		
	def getColumn(self):
		return copy.deepcopy(self.__column)

	def checkHorizontal(self, row, col, symbol):
		for next_index in range(1, 4):
			if self.board[row][col + next_index] != symbol:
				return False
		return True

	def checkVertical(self, row, col, symbol):
		for next_index in range(1, 4):
			if self.board[row - next_index][col] != symbol:
				return False
		return True

	def checkRightDiagonal(self, row, col, symbol):
		for next_index in range(1, 4):
			if self.board[row - next_index][col + next_index] != symbol:
				return False
		return True

	def checkLeftDiagonal(self, row, col, symbol):
		for next_index in range(1, 4):
			if self.board[row - next_index][col - next_index] != symbol:
				return False
		return True

	def win(self, player):
		symbol = player.getSymbol()
		for row in range(self.__row - 1, -1, -1):
			for col in range(self.__column - 1, -1, -1):
				if row - 3 >= 0:
					if self.checkVertical(row, col, symbol):
						return True
					if col + 3 <= self.__column - 1:
						if self.checkRightDiagonal(row, col, symbol):
							return True
					if col - 3 >= 0:
						if self.checkLeftDiagonal(row, col, symbol):
							return True
				if col + 3 <= self.__column - 1:
					if self.checkHorizontal(row, col, symbol):
							return True
		return False
