from Players.Player import *

class Human(Player):

	def __init__ (self):
		Player.__init__(self,"Human");
		
	def Play(self):
		if self._myCurrentMove == 0:
			# Get my new current move.  This Player is controlled by a human player.
			print("\nSelect a Move from the list:")
			print("(1) : Rock")
			print("(2) : Paper")
			print("(3) : Scissors")
			print("(4) : Lizard")
			print("(5) : Spock")
			
			goodChoice = 0
			# Loop until a valid choice is selected (integer, 1-5)
			while goodChoice == 0:
				print("> ",end="")
				try: 
					myChoice = int(input())
				except ValueError:
					continue
		
				if 1 <= myChoice & myChoice <= 5 :
					goodChoice = 1

			self._myCurrentMove = {
				1: self.pRock,
				2: self.pPaper,
				3: self.pScissors,
				4: self.pLizard,
				5: self.pSpock,
			}[myChoice]

		
		return self._myCurrentMove

		