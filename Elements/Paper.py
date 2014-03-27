from Elements.Element import *

class Paper(Element):

	Draw = [
		"                  `..,,..`                  ",
		"             .,` `````````` `,`             ",
		"          `, ```````````````````,`          ",
		"        ..````````````````````````.`        ",
		"       .`````````````````````; ``  `,       ",
		"     .``````````````````` '    ,    ``.     ",
		"    , ``````````````````:         ```` .    ",
		"   , `````````````````.     ;    #.```` .   ",
		"  . `````````````` ` :    ;     :  ```````  ",
		"  .``````````  ::  '     `          `````.  ",
		" ,``````````;    ;     '     '     ```````. ",
		" .```````` .   '      `     .    ':```````. ",
		"` ```````    ;            '    .`  ```````` ",
		".```````,  ,                  ;   +``````` `",
		".``````` ;                   ,   +`````````.",
		".``````;                   ;    ;``````````.",
		".``````                   +    ``````````` `",
		"  ````:                      , ```````````` ",
		" .```.                      +`````````````, ",
		" .```+                     +````````````` ` ",
		"  . '                     +``````````````,  ",
		"                         ```````````````.   ",
		"   `                   '````````````````    ",
		"    .                ; ```````````````.     ",
		"                   . ````````````````,      ",
		"       .         .``````````````````.       ",
		"         .     ' `````````````````,         ",
		"           .; `````````````````,`           ",
		"              `,.`  ````  `.,`              ",
	]

	def __init__ (self):
		Element.__init__(self,"Paper");
		
	def compareTo(self,ct):
		if ct.name() == "Rock":
			return "Paper covers Rock","Win"
		elif ct.name() == "Paper":
			return "Paper equals Paper","Tie"
		elif ct.name() == "Scissors":
			return "Scissors cuts Paper","Lose"
		elif ct.name() == "Lizard":
			return "Lizard eats Paper","Lose"
		elif ct.name() == "Spock":
			return "Paper disproves Spock","Win"
		else:
			return "Error","No winner"
			
	def getInt(self):
		return 1
