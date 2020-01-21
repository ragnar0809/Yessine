from random import *
nums = randrange(21)
guess = int(input("Guess a number between 0 and 20: "))
if guess == nums :
	print("Right guess")
elif guess > nums :
	print("Your guess is too high!")
else:
	print("Your guess is too low!")
print("The Number is: ", nums)

