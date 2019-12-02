import sys

rows = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


def drawTablep1(player1_choice):


	rows[player1_choice-1] = "X"

	print (rows[0], "|", rows[1], "|", rows[2],"\n")
	print (rows[3], "|", rows[4], "|", rows[5],"\n")
	print (rows[6], "|", rows[7], "|", rows[8],"\n")






def drawTablep2(player2_choice):

	rows[player2_choice-1] = "O"

	print (rows[0], "|", rows[1], "|", rows[2],"\n")
	print (rows[3], "|", rows[4], "|", rows[5],"\n")
	print (rows[6], "|", rows[7], "|", rows[8],"\n")



def count():
	win = "you have 3 in a row - P1 Wins"
	print(rows)
#	Horizontal X

	if rows[0] == "X" and rows[1] == "X" and rows[2] == "X":
		print(win)
		sys.exit()
	elif rows[3] == "X" and rows[4] == "X" and rows[5] == "X":
		print(win)
		sys.exit()

	elif rows[6] == "X"  and rows[7] == "X" and rows[8] == "X":
		print(win)
		sys.exit()

#	Vertical X
	elif rows[0] == "X" and rows[3] == "X" and rows[6] == "X":
		print(win)
		sys.exit()
	elif rows[1] == "X" and rows[4] == "X" and rows[7] == "X":
		print(win)
		sys.exit()
	elif rows[2] == "X" and rows[5] == "X" and rows[8] == "X":
		print(win)
		sys.exit()

#	Diagonal X
	elif rows[0] == "X" and rows[4] == "X" and rows[8] == "X":
		print(win)
		sys.exit()

	elif rows[6] == "X" and rows[4] == "X" and rows[2] == "X":
		print(win)
		sys.exit()

#       Horizontal O
	elif rows[0] == "O" and rows[1] == "O" and rows[2] == "O":
		print(win)
		sys.exit()

	elif rows[3] == "O" and rows[4] == "O" and rows[5] == "O":
		print(win)
		sys.exit()

	elif rows[6] == "O" and rows[7] == "O" and rows[8] == "O":
		print(win)
		sys.exit()

#       Vertical O
	elif rows[0] == "O" and rows[3] == "O" and rows[6] == "O":
		print(win)
		sys.exit()

	elif rows[1] == "O" and rows[4] == "O" and rows[7] == "O":
		print(win)
		sys.exit()
	elif rows[2] == "O" and rows[5] == "O" and rows[8] == "O":
		print(win)
		sys.exit()

#       Diagonal O
	elif rows[0] == "O" and rows[4] == "O" and rows[8] == "O":
		print(win)
		sys.exit()

	elif rows[6] == "O" and rows[4] == "O" and rows[2] == "O":
		print(win)
		sys.exit()








a=1
while a==1:
	try:
		while True:
			player1_choice = int(input("Player 1, choose from 1-9 "))

			if rows[player1_choice-1] == "_":
				drawTablep1(player1_choice)
				count()
				break
			else:
				print("Pick another number")


	except Exception:
		print("Pick a number - ex1")
		continue
	try:

		while True:
			try:
				player2_choice = int(input("Player 2, choose from 1-9 "))

				if rows[player2_choice-1] == "_":
					drawTablep2(player2_choice)
					count()
					break
				else:
					print("Pick another number")
			except Exception:
				print("ex3")
				continue

	except Exception:
		print("Pick a number - ex2")
		continue
