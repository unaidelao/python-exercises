#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercise 2: Odd or Even.

Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
"""

__author__ = "Unai de la O"
__license__ = "MIT"


def print_result(user_number):
    """Function that prints if user's number is ODD or EVEN."""
    if user_number % 2 == 0:
        print("Your number is EVEN.")
    else:
        print("Your number is ODD.")


print("Enter a number, please:")
user_number = int(input("> "))

print_result(user_number)
