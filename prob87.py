# Problem 87 - Number Guessing Logic

import random

secret_number = random.randint(1, 100)
guess = -1
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too low, try again")
    elif guess > secret_number:
        print("Too high, try again")
    else:
        print("Correct! You guessed in", attempts, "attempts")
