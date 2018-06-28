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

	def findRow(self, insert_column, player):
		for i in range(self.__row - 1, -1, -1):
			if self.board[i][insert_column] == '.':
				self.board[i][insert_column] = player.getSymbol()
				return i
      
	def getRow(self):
		return copy.deepcopy(self.__row)
		
	def getColumn(self):
		return copy.deepcopy(self.__column)
	
	def isFull(self):
		return all(i != '.' for i in self.board[0])

class Player:
	
	def __init__(self, player_num, symbol, player):
		self.__playerNum = player_num
		self.__symbol = symbol
		self.__moves = [[] for x in range(7)]
		self.__name = player
		
	def getPlayerName(self):
		return copy.deepcopy(self.__name)
	
	def getPlayerNum(self):
		return copy.deepcopy(self.__playerNum)
	
	def getSymbol(self):
		return copy.deepcopy(self.__symbol)

	def getMoves(self):
		return copy.deepcopy(self.__moves)
		
	def addMoves(self, row, column):
		self.__moves[column].append(row) 
		
	def checkWin(self):
		if self.checkHorizontal() or self.checkVertical() or self.checkDiagonal1() or self.checkDiagonal2():
			return True

	def checkHorizontal(self):
		num = 0
		for i in range(len(self.__moves) - 3):
			for j in range(len(self.__moves[i])):
				index = i
				num = self.__moves[i][j]
				count = 1
				for k in range(1,4):
					try:
						for item in self.__moves[index+k]:
							if item == num:
								count += 1
					except:
						break
				if count == 4:
					return True
		return False
		
	def checkVertical(self):
		num = 0 
		for i in range(len(self.__moves)):
			if len(self.__moves[i]) >= 4:
				for j in range(len(self.__moves[i])):
					count = 1
					index = j
					num = self.__moves[i][index]
					for k in range(1,4):
						try:
							if self.__moves[i][index + k] == (num - k):
								count += 1
							else:
								break
						except:
							break
					if count == 4:
						return True
		return False
		
	def checkDiagonal1(self):
		for i in range(len(self.__moves)):
			if len(self.__moves[i]) > 0:
				for j in range(len(self.__moves[i])):
					index = j
					num = self.__moves[i][j]
					count = 1
					for k in range(1,4):
						try:
							for item in self.__moves[i+k]:
								if item == num-k:
									count+=1
						except:
							break
					if count == 4:
						return True
		return False
		
	def checkDiagonal2(self):
		for i in range(len(self.__moves)):
			if len(self.__moves[i]) > 0:
				for j in range(len(self.__moves[i])):
					index = j
					num = self.__moves[i][j]
					count = 1
					for k in range(1,4):
						try:
							for item in self.__moves[i+k]:
								if item == num+k:
									count+=1
						except:
							break
					if count == 4:
						return True
		return False
	
		