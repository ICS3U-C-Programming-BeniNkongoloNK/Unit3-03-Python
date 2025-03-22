#!/usr/bin/env python3
# Created By: Beni
# Date: March 22, 2025
# Guesses random number

import random

def main():
    guess = int(input("Hello, try guessing my number. You won't get it this time: "))
    correct_guess = random.randint(0,9)
    if guess == correct_guess:
        print("You got lucky this time!")
    else:
        print("See I told you you wouldn't get it. The number was {}!".format (correct_guess))


if __name__ == "__main__":
    main()