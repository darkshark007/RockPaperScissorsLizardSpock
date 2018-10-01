from Players.Player import *
from random import Random

class StupidBot(Player):

	def __init__ (self):
		Player.__init__(self,"StupidBot");
		
	def Play(self):
		if self._myCurrentMove == 0:
			# Get my new current move.  This bot is stupid, so always picks the same thing over and over again.  It selects this move at random.
			r = Random()
			myChoice = r.randint(1,5)
			self._myCurrentMove = {
				1: self.pRock,
				2: self.pPaper,
				3: self.pScissors,
				4: self.pLizard,
				5: self.pSpock,
			}[myChoice]

		
		return self._myCurrentMove

	def Update(self):
		# Update my Move statuses
		self._myLastMove = self._myCurrentMove
	