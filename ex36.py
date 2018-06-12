import os 
import platform
import sys
import random

def start():

	print("""
			WELCOME FROM MY GAME
			HAVE FUN!
		""")	
	print("""
			CHOOSE ONE ROOM TO PLAY
			=======================
			1.Room One
			2.Room Two
			3.Room Three
		""")

	rooms = {
	"1" : room_one,
	"2" : room_two,
	"3" : room_three,
	}

	choice = input("> ")

	action = rooms.get(choice,None)

	if not action:
		print("Invalid room choice")

	else: 
		action()

def clear_screen():

	os_type = platform.system()

	if os_type == 'Linux':
		os.system('clear')
	if os_type == 'Windows':
		os.system('cls')

def room_one():

	clear_screen()
	print("""
			WELCOME FROM ROOM ONE
			=====================
		""")

	print("This room is full of gold. How much do you take?")

	choice = input("> ")
	gold_amount = 0 

	if "0" in choice or "1" in choice:
		gold_amount = int(choice)
	else: 
		loser("You should enter a valid number")

	if gold_amount < 20 : 
		winner("You are not greedy. You win the game!")
	else: 
		loser("You are greedy. You lose the game!")



def room_two():
	clear_screen()
	print("""
			WELCOME FROM ROOM TWO
			=====================
		""")
	print("""
			Rules
			-------------------------------
			In this room, you must a number.
			The game generate a number randomly between 2 and 21.
			And the number is divided by 2.
			When your input number is equal to the quotient , you win the game!
		""")	

	input_num = int(input("> "))

	random_num = random.randint(2,21)
	the_ans = int(random_num / 2)
	
	if input_num == the_ans: 
		winner("You win the game.")
	else: 
		loser("You lose the game")

def room_three():
	clear_screen()
	print("""
			WELCOME FROM ROOM THREE
			=======================
		""")

	print("""
			Rules
			---------------------------------------------------------
			In the room three, player must roll a die for three times.
			When your value is greater than 3 after rolling the die for three times, you win the game.
		""")
	input("Press enter to start! ")

	i = 1
	total = 0 
	while i <= 3: 
		print(f"Roll the die for {i} time")
		input("> ")
		value = random.randint(1,6)
		print(f"The value for the {i} time is {value}")

		total += value 
		i += 1

	result = int(total/3)

	if result < 3: 
		loser("Your value is less than 3")
	else: 
		winner("You win the game.")

def loser(message=''):

	if message != '':
		print(message)

	print("Game terminated!")
	sys.exit(0)

def winner(message=''):

	if message != '':
		print(message)
	print("""
			Congratulation! You are the winner.
			Thank you for playing my game.
		""")
	sys.exit(0)

if __name__ == '__main__':

	start()



