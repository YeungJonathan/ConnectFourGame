from connect4_board import Board
from connect4_player import Player

b = Board()
p1 = Player(1, 'X')
p2 = Player(2, 'O')

def promptInput():
	userinput = int(input('Please input column to insert: '))
	return userinput

while True:
	print("Player1's turn")
	userinput = promptInput()
	b.insert(userinput, p1)
	print(b)
	if b.win():
		print("Player1 wins!")
		break
		
	userinput = promptInput()
	print("PLayer2's turn")
	b.insert(userinput, p2)
	print(b)
	if b.win():
		print("Player2 wins!")
		break
