import copy
class player:
	
	def __init__(self, player_num = 1):
		self.__playerNum = player_num
	
	def getPlayerNum(self):
		return copy.deepcopy(self.__playerNum)