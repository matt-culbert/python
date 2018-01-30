class Board:
	# the class has functions which compare move coordinates to the destination square
	# has functions which take in coordinates to move too and compare with the rest of the board
	def __init__(self):
		dictPos = {} # dict to hold other pieces position

	def moveTo(self, current_pos, dest_pos):

	def updateDictPost(self, pos, color):
		self.dictPos[color] = pos

class Pieces:
	# has functions for each different piece which has their move coordinates 
	def knight(self):
		moves = x+3
		moves2 = y+1