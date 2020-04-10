from Players.Player import *

class LastPlayBot(Player):

	def __init__ (self):
		Player.__init__(self,"LastPlayBot");
		
	def Play(self):
		if self._myCurrentMove == 0:
			# Get my new current move.  This bot always picks the choice the opponent last picked.
			if self._myOpponent._myLastMove == 0:
				# If the opponent hasnt played any moves yet, then just pick Spock.
				self._myCurrentMove = self.pSpock
			else:
				self._myCurrentMove = self._myOpponent._myLastMove

		return self._myCurrentMove
		