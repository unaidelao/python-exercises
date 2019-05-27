#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercise 4: Divisors.

Create a program that asks the user for a number and then prints out a list of all the divisors
of that number.
"""

# Ask user for a number.
print("Enter a number that you want to know its divisors:")
user_number = int(input("> "))

# Create a list with all possible divisors of user_number.
possible_divisors = list(range(user_number, 0, -1))

# List of divisors.
divisors = []

# Check possible divisors.
for div in possible_divisors:
    if user_number % div == 0:
        divisors.append(div)

# Print results.
print(f"The divisors of {user_number} are: {divisors}")

# Extra info.
if len(divisors) == 2:
    print(f"So, {user_number} is a PRIME number.")
