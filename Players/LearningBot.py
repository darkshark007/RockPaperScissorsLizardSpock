from Players.Player import *
from Lib.random import Random

class LearningBot(Player):

	def __init__ (self):
		Player.__init__(self,"LearningBot");
		
		# Build the Outcome table using a pseudo-array list
		self._outcomeTable = [5]
		''' # Method 1
		for i in range(len(self._outcomeTable)):
			list = [5]
			for j in range(len(list)):
				list2 = [5]
				list[j] = list2
			self._outcomeTable[i] = list
		'''
		
		''' # Method 2
		for i in range(5):
			self._outcomeTable[i] = [5]
			for j in range(5):
				self._outcomeTable[i][j] = [5]
		'''
		
		# Method 3
		self._outcomeTable = [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]
		

	def Play(self):
		if ( self._myCurrentMove == 0):
			r = Random()
			# Get my new current move.  This bot attempts to learn its opponents habits, assessing their reponse to its picks and their own picks.
			
			# Check to see if this is the first turn.
			if ( self._myLastMove == 0 ):
				# If this is the first turn, pick a random move.
				CM = {
					1: self.pRock,
					2: self.pPaper,
					3: self.pScissors,
					4: self.pLizard,
					5: self.pSpock,
				}[r.randint(1,5)]
			else:
				moveStrength = [0,0,0,0,0]
				# First, we're going to calculate the Move Strength of each possible move based on the opponents previous history of move selection, based on the opponents latest pick in response to the previous round.
				
				for i in range(5):
					for j in range(5):
						#print(str(i)+","+str(self._myOpponent._myLastMove.getInt())+","+str(j))
						#print(moveStrength[j])
						moveStrength[j] += self._outcomeTable[i][self._myOpponent._myLastMove.getInt()][j] * 1.00 # Loop over all the possible combinations based on Opponents last pick
						moveStrength[j] += self._outcomeTable[self._myLastMove.getInt()][i][j] * 1.50 # Loop over all the possible combinations based on this bots last pick
					moveStrength[i] += self._outcomeTable[self._myLastMove.getInt()][self._myOpponent._myLastMove.getInt()][i] * 2.00 # Loop over all the possible combinations based on this bots and the opponents last pick
					

				# Now that the move weights have all been quantified, select the highest one.  This represents the "most likely" choice the opponent will select this round, based on the current state the history of previous states.
				highest = r.randint(0,4)
				for i in range(5):
					if ( moveStrength[i] > moveStrength[highest] ):
						highest = i
				
				CM = {
					0: self.pRock,
					1: self.pPaper,
					2: self.pScissors,
					3: self.pLizard,
					4: self.pSpock,
				}[highest]
				
				#print("Selected "+str(CM)+": "+str(moveStrength[highest]))
				#print(self._outcomeTable)

			# Next, now that i have the opponents likely choice, decide on a move that will win against it.  Select this move randomly, and then test its result, until a suitable choice is selected.
			myChoice = r.randint(1,5)
			self._myCurrentMove = {
				1: self.pRock,
				2: self.pPaper,
				3: self.pScissors,
				4: self.pLizard,
				5: self.pSpock,
			}[myChoice]
			while self._myCurrentMove.compareTo(CM)[1] != "Win":
				myChoice = r.randint(1,5)
				self._myCurrentMove = {
					1: self.pRock,
					2: self.pPaper,
					3: self.pScissors,
					4: self.pLizard,
					5: self.pSpock,
				}[myChoice]

			# Update the outcome table
			# Make sure this isnt the first turn.
			if self._myLastMove != 0:
				# Make sure the opponent has made a move.
				if self._myOpponent._myCurrentMove == 0:
					self._myOpponent.Play()
				#print(str(self._myLastMove.getInt())+", "+str(self._myOpponent._myLastMove.getInt())+", "+str(self._myOpponent._myCurrentMove.getInt()))
				self._outcomeTable[self._myLastMove.getInt()][self._myOpponent._myLastMove.getInt()][self._myOpponent._myCurrentMove.getInt()] += 1
				#print(self._outcomeTable[self._myLastMove.getInt()])
					
			
				
		return self._myCurrentMove
		