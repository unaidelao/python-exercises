#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercise 3: List Less Than Ten.

Take a list, say for example this one:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""

a = [1, 6, 78, 3, 5, 8, 11, 12, 4, 2, 79, 4, 43, 34, 2, 1, 2]

# Prints out all elements that are less than 5.
for number in a:
    if number < 5:
        print(number)


# Extra: Instead of printing the elements one by one, make a new list that has all the
# elements less than 5 from this list in it, and print out this new list.
new_list = []
for number in a:
    if number < 5:
        new_list.append(number)

print(f"\nThe new list with numbers < 5 is: {new_list}")

# Extra: Write that in one line of Python.
new_list2 = [elem for elem in a if int(elem) < 5]
print(f"\nSame as above but in one line of code: {new_list2}\n")

# Extra: Ask the user for a number and return a list that contains only elements from the
# original list that are smalles than that number given by the user.
print("Enter a filter(integer):")
filter = int(input("> "))

new_list3 = [elem for elem in a if int(elem) < filter]
print(f"Filtered list as you wish: {new_list3}")
