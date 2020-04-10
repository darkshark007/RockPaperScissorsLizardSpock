# Element Class -- Will be super-class to all of the game options.
class Element(object):

	# [Instance Variables]
	#	 _name			-- Name of the Element

	def __init__ (self,nm):
		self._name = nm
		
	def __str__(self):
		return "["+self._name+"]"
		
	def name(self):
		return self._name
		
	def compareTo(self,ct):
		raise NotImplementedError("Not yet implemented")
		
	def getInt(self):
		raise NotImplementedError("Not yet implemented")
