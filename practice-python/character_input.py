#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercise 1: Character Input.

Create a program that asks the user to enter their name and their age.

Print out a message addressed to them that tells them the year that they
will turn 100 years old.
"""

__author__ = "Unai de la O"
__license__ = "MIT"

from datetime import datetime


def calc_100_years_old(age):
    actual_year = datetime.now().year
    return actual_year + (100 - age)


print("Please, enter your name:")
name = input("> ")
print("Now, enter your age, please:")
age = int(input("> "))

print(f"The year you will turn 100 years old: {calc_100_years_old(age)}")
