from Elements.Element import *
from Elements.Rock import *
from Elements.Paper import *
from Elements.Scissors import *
from Elements.Lizard import *
from Elements.Spock import *
from Players.StupidBot import *
from Players.RandomBot import *
from Players.IterativeBot import *
from Players.LastPlayBot import *
from Players.Human import *
from Players.CheaterBot import *
from Players.JonsBot import *
from Players.LearningBot import *
from Players.LearningBot_2 import LearningBot as lb2
from time import sleep
import os
import sys

# Main function script.  Not sure if this must be made into a Main-type function, or if an imperative-esque script is sufficient enough for this, but im doing it this way anyway.

# Define a console clear function.  It just makes the game look so much cleaner!  Although, it also seems to create some weird behavior if the game is viewed anywhere but a windows command line.
clear = lambda: os.system('cls')


# Define some global variables
bot1 = 0
bot2 = 0
playLoop = 0
playLoopAutoGap = .35
playLoopHumanGap = 3.50

while (True):
	if bot1 == 0:
		# If the players havent been selected yet, then force the 'n' option to prompt the user to select players.
		myChoice = "n"
	# Check to see if control is currently auto-looping.
	elif playLoop > 0:
		if ( bot1.name() == "Human" ) | ( bot2.name() == "Human" ):
			sleep(playLoopHumanGap)
		else:
			if playLoop > 10:
				playLoopGap -= .01
			if ( playLoopGap > 0 ):
				sleep(playLoopGap)

		playLoop -= 1
		myChoice = "p"
	else:
		# Otherwise, print the standard options as normal.
		print("\r\n\r\nSelect an option:")
		print("(p) : Play a round")
		print("(m) : Play many rounds successively")
		print("(n) : Select new Players")
		print("(q) : Quit the application")
		print("> ",end="")
		myChoice = input()


	# This flag triggers the auto-loop, commiting human players to play the specified number of rounds, or running and reporting the specified number of rounds between bots without interruption.
	if myChoice == "m" or myChoice == "M":
		playLoopGap = playLoopAutoGap
		print("How many rounds would you like to play?\r\n> ",end="")
		while (True):
			try: 
				playLoop = int(input())
				break
			except ValueError:
				continue

	# This flag resets the scores and selects new players.  This block is also called automatically in the first loop.
	elif myChoice == "n" or myChoice == "N":
		clear()
		
		gameRound = 1
		Pl1Score = 0
		Pl2Score = 0

		# If bots is undefined, then this is the first time players are selected...
		if bot1 == 0:
			# ...so, display this extra message.
			print("Welcome to Rock, Paper, Scissors, Lizard, Spock, implemented by Stephen Bush.\r\n   (Note:  This game is best viewed on the command line, with a width of at least 100 characters.)")
		print("\r\nList of available Players:")
		print("-----------------------------------------------------------")
		print("(1) : Human")
		print("(2) : StupidBot")
		print("(3) : RandomBot")
		print("(4) : IterativeBot")
		print("(5) : LastPlayBot")
		print("(6) : CheaterBot")
		print("(7) : LearningBot")
		print("(8) : JonsBot")

		print("\r\nSelect player #1")
		goodChoice = 0
		while goodChoice == 0:
			print("> ",end="")
			try: 
				myChoice = int(input())
			except ValueError:
				continue

			if 1 <= myChoice and myChoice <= 8 :
				goodChoice = 1

		bot1 = {
			1: Human(),
			2: StupidBot(),
			3: RandomBot(),
			4: IterativeBot(),
			5: LastPlayBot(),
			6: CheaterBot(),
			7: LearningBot(),
			8: JonsBot(),
		}[myChoice]

		print("\r\nSelect player #2")
		goodChoice = 0
		while goodChoice == 0:
			print("> ",end="")
			try: 
				myChoice = int(input())
			except ValueError:
				continue

			if 1 <= myChoice and myChoice <= 8 :
				goodChoice = 1

		bot2 = {
			1: Human(),
			2: StupidBot(),
			3: RandomBot(),
			4: IterativeBot(),
			5: LastPlayBot(),
			6: CheaterBot(),
			7: LearningBot(),
			8: JonsBot(), # lb2(), 
		}[myChoice]

		bot1.setOpponent(bot2);
		bot2.setOpponent(bot1);

	# This flag triggers the play of one round.
	elif myChoice == "p" or myChoice == "P":
		clear()
		pick1 = bot1.Play();
		clear()
		pick2 = bot2.Play();
		clear()
		Round = pick1.compareTo(pick2)
		print("\r\n  Game Round "+str(gameRound)+"\r\n\r\n")
		
		
		# Print the Element images
		i = 0
		while i < 29:
			print("  "+pick1.Draw[i]+"        "+pick2.Draw[i])
			i += 1
		
		# Print the round results.
		print("\r\n "+str(bot1.name()+" Picks:  "+str(pick1)).center(45)+"        "+str(bot2.name()+" Picks:  "+str(pick2)).center(45)+"\r\n")
		gameRound += 1
		print(str(Round[0]).center(99))
		if Round[1] == "Win":
			Pl1Score += 1
			print(str("Player 1 Wins!!").center(99))
		elif Round[1] == "Lose":
			Pl2Score += 1
			print(str("Player 2 Wins!!").center(99))
		else:
			print(str("Tie!!").center(99))
			
		# Report the current score
		print("  Current Score:\r\n    "+str(Pl1Score)+" -- "+str(Pl2Score))

		bot1.Update()
		bot2.Update()
	elif myChoice == "q" or myChoice == "Q":
		print("\r\nGoodbye, thanks for playing!!")
		break
	
	# This is a special hidden flag that turns off all of the gaps built in for readability, allowing many trials to be run quickly.
	elif myChoice == "--NoGap":
		playLoopAutoGap = 0
		playLoopHumanGap = 0

