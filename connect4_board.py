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
			string += "\n"
		return string

	def printPretty(self):
		for item in self.board:
			for position in item:
				print(position, end=" ")
			print("")
	
	def getRow(self):
		return copy.deepcopy(self.__row)
		
	def getColumn(self):
		return copy.deepcopy(self.__column)
<<<<<<< HEAD

	#TODO: method will take a player argument to check for player's symbol
	#TODO: refactor horizontal, vertical, and diagonal checks
	def win(self):
		for i in range(len(self.board) - 3):
			for j in range(len(self.board[i]) - 3):
				if self.board[i][j] == 'O':
					#check horizontal
					if self.board[i][j+1] == 'O' and self.board[i][j+2] == 'O' and self.board[i][j+3] == 'O':
						return True
					#check vertical
					if self.board[i + 1][j] == 'O' and self.board[i + 2][j] == 'O' and self.board[i + 3][j] == 'O':
						return True
					#check diagonals
					if self.board[i + 1][j + 1] == 'O' and self.board[i + 2][j + 2] == 'O' and self.board[i + 3][j + 3] == 'O':
						return True
					return False
				elif self.board[i][j] == 'X':
					#check horizontal
					if self.board[i][j+1] == 'X' and self.board[i][j+2] == 'X' and self.board[i][j+3] == 'X':
						return True
					#check vertical
					if self.board[i + 1][j] == 'X' and self.board[i + 2][j] == 'X' and self.board[i + 3][j] == 'X':
						return True
					#check diagonals
					if self.board[i + 1][j + 1] == 'X' and self.board[i + 2][j + 2] == 'X' and self.board[i + 3][j + 3] == 'X':
						return True
					return False


a = Board(7,8)
print(a)
=======
	
	def insert(self, insert_column, player):
		for i in range(self.getRow()-1, -1, -1):
			if self.board[i][insert_column] == '.':
				self.board[i][insert_column] = player.getSymbol()
				return
		
>>>>>>> 06b64cda0416d2de9c338ff24f0da448ee655e00
