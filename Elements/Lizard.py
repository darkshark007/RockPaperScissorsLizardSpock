from Elements.Element import *
from termcolor import colored

class Lizard(Element):

	Draw = [
		"                  `.,,,,.`                  ", 
		"             `:.````````````.:.             ",
		"           :````````````````````,.          ",
		"        `,````````````````````````..        ",
		"       :````````````````````````````,       ",
		"     `.```````````````````````````````,     ",
		"    ,``````````````````````````````````:    ",
		"   .````````````````````````````````````:   ",
		"   .````````````````'+'.  ,;;` ;;````````,  ",
		"  ,````````````,#:              ,, '`````.  ",
		" .``````````,,                     ..,````: ",
		" ,``````````'          :,:;:,,,.:. `;`````. ",
		" .``````````@       ,;`  :':..  ,;#````````.",
		"````````````#      #..````````:    ````````,",
		".```````````        '````````:    `````````,",
		".``````````+          '````,:    ;`````````,",
		"```````````                      ``````````,",
		" .````````;                    ;````````````",
		" :````````                  :`````````````, ",
		" ```````,                 '```````````````, ",
		"  :````+                '````````````````,  ",
		"   ,```               '```````````````````  ",
		"    ;               '```````````````````.   ",
		"                ,;,````````````````````.    ",
		"      `       '``````````````````````,      ",
		"       ,     .``````````````````````:       ",
		"         , +``````````````````````:         ",
		"           .,``````````````````,,           ",
		"              `:,.`````````,:.              ",
	]

	def __init__ (self):
		Element.__init__(self,"Lizard");
		
	def compareTo(self,ct):
		if ct.name() == "Rock":
			return "Rock smashes Lizard","Lose"
		elif ct.name() == "Paper":
			return "Lizard eats Paper","Win"
		elif ct.name() == "Scissors":
			return "Scissors decapitate Lizard","Lose"
		elif ct.name() == "Lizard":
			return "Lizard equals Lizard","Tie"
		elif ct.name() == "Spock":
			return "Lizard poisons Spock","Win"
		else:
			return "Error","No winner"

	def getInt(self):
		return 3
	
	