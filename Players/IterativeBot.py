from Players.Player import *
from Lib.random import Random

class IterativeBot(Player):

	def __init__ (self):
		Player.__init__(self,"IterativeBot");
		
		# This bot selects a random start point.
		r = Random()
		self._myCurrentChoice = r.randint(0,4)
		
	def Play(self):
		if self._myCurrentMove == 0:
			# Get my new current move.  This bot iteratively selects moves in a known order.
			self._myCurrentChoice = ( self._myCurrentChoice + 1 ) % 5
			self._myCurrentMove = {
				0: self.pRock,
				1: self.pPaper,
				2: self.pScissors,
				3: self.pLizard,
				4: self.pSpock,
			}[self._myCurrentChoice]
		
		return self._myCurrentMove
		