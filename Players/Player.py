from Elements.Rock import *
from Elements.Paper import *
from Elements.Scissors import *
from Elements.Lizard import *
from Elements.Spock import *

# Player Class -- Will be super-class to all of the player options
class Player(object):

	# [Instance Variables]
	#	 _name			   -- Name of the Element
	#    _myLastMove       -- The last move that this player used
	#    _myCurrentMove    -- The current move that this player is using.
	#    _myOpponent       -- The opponent i am playing against
	
	# Define the static move variables
	pRock = Rock()
	pPaper= Paper()
	pScissors= Scissors()
	pLizard = Lizard()
	pSpock = Spock()
	
	def __init__ (self,nm):
		self._name = nm
		self._myCurrentMove = 0
		self._myLastMove = 0
		
	def __str__(self):
		return "["+self._name+"]"
		
	def name(self):
		return self._name
		
	def getCurrentMove(self):
		return self._myCurrentMove
		
	def getLastMove(self):
		return self._myLastMove
		
	# This method is used to assign an "opponent" player reference to this player, allowing this player to collect information about it's opponents selections.
	def setOpponent(self,opp):
		self._myOpponent = opp
		
	def Play(self):
		raise NotImplementedError("Not yet implemented")
		
	def Update(self):
		# Update my Move statuses.  This method resets the player after each "turn", performing whatever functions are necessary to maintain the Players informational integrity.
		self._myLastMove = self._myCurrentMove
		self._myCurrentMove = 0
		
