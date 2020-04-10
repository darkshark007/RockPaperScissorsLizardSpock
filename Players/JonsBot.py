from Players.Player import *

# This bot is based off an idea by Jon Koenes
class JonsBot(Player):

	def __init__ (self):
		Player.__init__(self,"JonsBot");
		
	def Play(self):
		if self._myCurrentMove == 0:
			# Get my new current move.  This bot always picks the counter-move of move of the opponents last move.  That is, it examines the opponents last move, and selects the move which beats both of the moves which beat that last move.
			if self._myOpponent._myLastMove == 0:
				# If the opponent hasnt played any moves yet, then just pick Spock.
				self._myCurrentMove = self.pRock
			else:
				self._myCurrentMove = self._myOpponent._myLastMove
				
			# Starting from the opponents last move, swap it with the counter-move of that move.
			self._myCurrentMove = {
				0: self.pLizard,
				1: self.pRock,
				2: self.pPaper,
				3: self.pSpock,
				4: self.pScissors,
			}[self._myCurrentMove.getInt()]

		return self._myCurrentMove
		