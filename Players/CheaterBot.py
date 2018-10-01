from Players.Player import *
from random import Random

class CheaterBot(Player):

	def __init__ (self):
		Player.__init__(self,"CheaterBot");
		
	def Play(self):
		if self._myCurrentMove == 0:
			r = Random()
			# Get my new current move.  This bot cheats, and always waits for the other player to select its move first, then it counters with a winning move.
			if self._myOpponent._myCurrentMove == 0:
				# If the opponent hasnt decided on a move yet, "wait" for them to decide.
				if self._myOpponent.name() == "CheaterBot":
					# Uh-oh.  The opponent is a CheaterBot, too.  Remember, cheaters never win.  Select a random move, and then both bots will play the same move, forever doomed to tie.
					myChoice = r.randint(1,5)
					self._myCurrentMove = {
						1: self.pRock,
						2: self.pPaper,
						3: self.pScissors,
						4: self.pLizard,
						5: self.pSpock,
					}[myChoice]
					# Echo this choice to the opponent, forcing them to play it also.
					self._myOpponent._myCurrentMove = self._myCurrentMove
					return self._myCurrentMove

			CM = self._myOpponent.Play()

			# Next, now that i have the opponents choice, decide on a move that will win.
			myChoice = r.randint(1,5)
			self._myCurrentMove = {
				1: self.pRock,
				2: self.pPaper,
				3: self.pScissors,
				4: self.pLizard,
				5: self.pSpock,
			}[myChoice]
			# Loop until i land on a random move which wins against the opponents selection
			while self._myCurrentMove.compareTo(CM)[1] != "Win":
				myChoice = r.randint(1,5)
				self._myCurrentMove = {
					1: self.pRock,
					2: self.pPaper,
					3: self.pScissors,
					4: self.pLizard,
					5: self.pSpock,
				}[myChoice]
			
		return self._myCurrentMove
		