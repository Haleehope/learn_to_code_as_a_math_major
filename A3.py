# ###################################################################
# Guess the mystery number
# ###################################################################

# the first lines of code in any file are usually any libraries you need to import
# a library is a collection of pre-written, reusable code components that you can import and use in your code
# you can open the pre-written (source) code for the library by right clicking on the library name and "Go to definition"
# this is kind of a lot to read through though and you don't need to understand all of it

# import the random library to be able to generate random numbers
# technically, they are pseudorandom, not actually random (but you don't need to know that)
import random

# generate a secret random integer between 1 and 100
secret = random.randint(1, 100)

# create a guesses variable that you will increment to count the number of guesses it takes to find the secret number
guesses = 0

# use a while loop to input a guessed integer from the user
while True:
    guess = int(input("Guess a number from 1 to 100: "))
    guesses += 1 # this is the same as guesses = guesses + 1

    # print out if it's too low, too high, or the correct number
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        break # break out of the while loop if they got the correct number

# once they get the correct answer, print how many guesses it took them
print(f"You needed {guesses} guesses.") # this could also be written as print("You needed", guesses, "guesses.")

# print a message to encourage the user to keep playing
if guesses <= 7:
    print("Excellent guessing!")
else:
    print("Try to beat your score next time.")