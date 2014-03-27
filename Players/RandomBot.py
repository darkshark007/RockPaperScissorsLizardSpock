from Players.Player import *
from Lib.random import Random

class RandomBot(Player):

	def __init__ (self):
		Player.__init__(self,"RandomBot");
		
	def Play(self):
		if self._myCurrentMove == 0:
			# Get my new current move.  This bot chooses a random move for every turn.
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
		