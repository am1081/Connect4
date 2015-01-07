#connect 4 by Andrew Marshall
#Made for use with Monte Carlo searches

class connect4:
	
	board = None
	playerTurn = 'O'

	def __init__(self):
		self.board = [[] for i in range(8)]
		self.printGame()
		
		while True:	
			if self.playerAction():
				self.printGame()
				print 'turn for ' + self.playerTurn
			else:
				print 'player ' + self.playerTurn + ' wins'


	def printGame(self):
		boardString = '0123456\n'
		for row in reversed(range(7)):
			for col in self.board:
				try:
					boardString += str(col[row])
				except:
					boardString += ' '
			boardString += '\n'
		print boardString

	def playerAction(self):

		playerInput = raw_input("column no [0-6]: ")

		column = int(playerInput)

		#check the move is valid
		if len(self.board[column]) < 6 and column < 7: 
			#add the move to the board
			self.board[column].append(self.playerTurn)
			if self.winner(column):
				return False
			else:
				self.playerTurn = 'O' if self.playerTurn == 'X' else 'X'
				return True

		return True
		

	def winner(self,column):
		counter_X = 0
		counter_Y = 0
		counter_UD = 0
		counter_DD = 0

		#these are used for checking if squares are in the same row/col/diagonal as the last move
		row = len(self.board[column]) - 1
		coordDifference = column - row
		coordSum = column + row

		#loop through each square on the board. This could be more efficient by only looping through important squares
		for colIndex in range(len(self.board)):
			for rowIndex in range(len(self.board[colIndex])):

				#if the squre is the one from this turn we know it's the players and the counters can all be added
				if colIndex == column and rowIndex == row:
					counter_UD += 1
					counter_DD += 1
					counter_Y += 1
					counter_X += 1
				else:
					#check up diagonal
					if colIndex - rowIndex == coordDifference:
						counter_UD += 1 if self.board[colIndex][rowIndex] == self.playerTurn else 0

					#check down diagonal
					if colIndex + rowIndex == coordSum:
						counter_DD += 1 if self.board[colIndex][rowIndex] == self.playerTurn else 0

					#check Y
					if colIndex == column:
						counter_Y += 1 if self.board[colIndex][rowIndex] == self.playerTurn else 0
						
					#check X
					if rowIndex == row:
						counter_X += 1 if self.board[colIndex][rowIndex] == self.playerTurn else 0

				if counter_X > 3 or counter_Y > 3 or counter_DD > 3 or counter_UD > 3:
					return True

		return False


if __name__ == '__main__':
	connect4()