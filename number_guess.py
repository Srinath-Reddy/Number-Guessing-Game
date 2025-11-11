# 🎯 Number Guessing Game
# -----------------------
# A simple Python game where the user guesses
# a random number chosen by the computer.

import random  # for random number generation

# Step 1: Generate a random number between 1 and 10
number = random.randint(1, 10)

# Step 2: Initialize user's guess
guess = 0

print("Welcome to the Number Guessing Game! 🎲")
print("I'm thinking of a number between 1 and 10...")

# Step 3: Loop until user guesses correctly
while guess != number:
    guess = int(input("Enter your guess: "))

    # Step 4: Give feedback to user
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number!")
