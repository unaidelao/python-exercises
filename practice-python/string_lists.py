#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercise 6: String Lists.

Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards).
"""


def is_palindrome(text):
    text_reverse = text[::-1]
    if text.upper() == text_reverse.upper():
        return True

    return False


text1 = "ABBA"
text2 = "Hall"

print(f"Is {text1} a palindrome?: {is_palindrome(text1)}")
print(f"Is {text2} a palindrome?: {is_palindrome(text2)}")

# Let user enter a string to check if it is a palindrome.
print("Enter a string, so we can check if it is a palindrome:")
user_input = input("> ")
print(
    f"Is user string '{user_input}' a palindrome?: {is_palindrome(user_input)}")
