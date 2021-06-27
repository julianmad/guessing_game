import random
lista = []
def pokaż_wynik():
	if len(lista) <= 0:
		print("Please enter your anwser")
	else:
		print(f"The current high score is {min(lista)}")
def starting_game():
	rand_num = random.randint(1,50)
	print("Hi stranger, wanna play something?")
	player = input("Tell us your name mate: ")
	play = input(f"So {player}, are you ready to start this majestic adventure? (Write: Yes/No): ")	
	print("In case if you want to quit earlier, just type 'Q'")		
	attempts = 0
	while play[0].lower() == "y":
		try:
			guess = input("Now, you can act like clairvoyants do, beautiful man, pick the number from 1 to 50! : ") 
			if guess == "Q":
				break
			elif int(guess) < 1 or int(guess) > 50:
				raise ValueError("No no no no, why did you do this?!?!/1/1 Wrong number :(")
				
			elif int(guess) == 	rand_num:
				print("Perfect guess, you are so clever!!!")
				attempts += 1
				lista.append(attempts)
				print(f"It took you {attempts} attempts to come to this moment")
				play_again = input("Ok well, it was a good fun, would you like to play again? (Write: Yes/No)")
				attempts = 0
				pokaż_wynik()
				rand_num = random.randint(1,50)
				if play_again[0].lower() == "n":
					print("Thats fine, we will miss you, see you next time!")
					break
			elif int(guess) < rand_num:
				print("Actually your number is lower")
				attempts += 1 
			elif int(guess) > rand_num:
				print("This time your guess is higher")
				attempts += 1	
	
		except ValueError as err:
			print("OH FATAL MISTAKE, WRONG NUMBER, PLEASE JUST DON'T DO DIS")
			print(f"({err})")	
	else: 
		print("Thats fine, we will miss you, see you next time!")					
if __name__ == '__main__':
	starting_game()