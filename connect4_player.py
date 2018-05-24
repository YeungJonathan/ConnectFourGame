import copy
class player:
	
	def __init__(self, player_num = 1, symbol):
		self.__playerNum = player_num
		self.__symbol = symbol
	
	def getPlayerNum(self):
		return copy.deepcopy(self.__playerNum)
	
	def getSymbol(self):
		return copy.deepcopy(self.__symbol)
