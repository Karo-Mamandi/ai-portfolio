# Import the random module to generate random numbers
import random

# Generate a random number between 1 and 99 (1-100 exclusive of 100)
n = random.randrange(1, 100)

# Get the player's first guess
guess = int(input("Enter any number: "))

# Continue loop until the guess matches the random number
while n != guess:  # means if n is not equal to the input guess
    # Check if guess is smaller than the target number
    if guess < n:
        print("Too low")
        # Ask the player to guess again
        guess = int(input("Enter number again: "))

    # Check if guess is greater than the target number
    elif guess > n:
        print("Too high!")
        # Ask the player to guess again
        guess = int(input("Enter number again: "))

    # This else clause is redundant because the while condition handles equality
    # But if guess equals n, break out of the loop
    else:
        break

# Display success message when the correct number is guessed
print("you guessed it right!!")
