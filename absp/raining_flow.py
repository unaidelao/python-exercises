#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Raining control flow program"""

import time

is_raining_flag = False

print("Is raining? (y/n)")
answer = input("> ")

if answer == "n" or answer == "no":
    print("Go outside.")
elif answer == "y" or answer == "yes":
    print("Have umbrella?")
    answer2 = input("> ")

    if answer2 == "y" or answer2 == "yes":
        print("Go outside.")
    elif answer2 == "n" or answer2 == "no":
        is_raining_flag = True
        while is_raining_flag:
            print("Wait a while...")
            time.sleep(3)
            print("Is still raining?")
            answer3 = input("> ")
            if answer3 == "n" or answer3 == "no":
                print("Go outside.")
                is_raining_flag = False
            elif answer3 == "y" or answer3 == "yes":
                continue
