#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Guess the number game"""

import random

print("Please, enter your name:")
name = input("> ")
random_number = random.randint(1, 100)

print(f"Hello {name}! I'm thinking of a number between 1 and 100. ¿Can you guess it?\nYou have 7 attempts!")

# Ask user to guess random_number.
for guesses_counter in range(1, 8):
    print("Try it!:")
    user_guess = int(input("> "))

    if user_guess < random_number:
        print("Your guess is too LOW.")
    elif user_guess > random_number:
        print("Your guess is too HIGH.")
    else:
        break    # This condition is the correct one!

if user_guess == random_number:
    print(f"Hey {name}, you guessed the number in {guesses_counter} attempts!")
else:
    print(f"Oh, poor {name}, you failed! The number was {random_number}")
