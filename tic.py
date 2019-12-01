

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
	if rows[0] and rows[1] and rows[2] == "X":
		print ("you have 3 in a row - P1 Wins")
	if rows[0] and rows[1] and rows[2] == "O":
		print ("you have 3 in a row - P2 Wins")




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
