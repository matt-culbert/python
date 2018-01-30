class Board:
	# the class has functions which compare move coordinates to the destination square
	# has functions which take in coordinates to move too and compare with the rest of the board
	def __init__(self):
		dictPos = {} # dict to hold other pieces position
		chessBoard = [[1] * 8 for i in xrange(8)]

	def moveTo(self, current_pos, dest_pos):

	def updateDictPost(self, pos, color):
		self.dictPos[color] = pos

class Pieces:
	# has functions for each different piece which has their move coordinates 
	def knight(self):
		moves = x+3
		moves2 = y+1
		# move 2 has to be executed after move 1

def main():
	white = Pieces.knight


	Board.moveTo()