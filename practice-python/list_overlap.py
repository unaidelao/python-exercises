#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercise 5: List Overlap.

Take two lists, and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on two lists of
different sizes.

Extras:

- Randomly generate two lists to test this.
"""

import random


def generate_list(list_length):
    l = []
    for i in range(list_length):
        l.append(random.randint(1, 15))

    return l


list_a = generate_list(8)
list_b = generate_list(14)

print(f"list_a: {list_a}")
print(f"list_b: {list_b}")

# Check duplicates to add them to final_list.
final_list = []
for num in list_a:
    if num in list_b and num not in final_list:
        final_list.append(num)

# Print results.
print(f"Duplicated values are: {final_list}")
