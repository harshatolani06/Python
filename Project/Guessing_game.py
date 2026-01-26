import random

print("Hi!, Welcome to the Number Guessing Game\n You have 7 chances to guess the number. \n Let's Start the Game")
low = int(input("Enter the LowerBound Number: "))
high = int(input("Enter the UpperBound Number: "))

num = random.randint(low,high)
ch = 7
gc = 0

while gc < ch:
	gc = gc+1
	guess = int(input("Enter your Guess "))
	if guess == num :
		print("Correct! The Number is{num}. You Guessed in {gc} attempts.")
		break
	elif guess < num:
		print("Oops! The Number is Too Small, Try a Higher Number.")
	elif guess > num:
		print("Oops! The Number is Too Big, Try  Smaller Number.")
	elif gc >= ch and guess != num:
		print("Sorry! Your Chances is Finished, The Number Was {num}. \n Better Luck Next Time.")
	
		