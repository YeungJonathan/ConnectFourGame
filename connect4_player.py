import copy

class Player:
	
	def __init__(self, player_num, symbol):
		self.__playerNum = player_num
		self.__symbol = symbol
	
	def getPlayerNum(self):
		return copy.deepcopy(self.__playerNum)
	
	def getSymbol(self):
		return copy.deepcopy(self.__symbol)
