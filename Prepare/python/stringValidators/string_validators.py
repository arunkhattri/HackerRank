#!/usr/bin/env python3
"""
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""


def check_condition(some_str):
    str_list = list(some_str)
    alphan = False
    alphabets = False
    digits = False
    lowers = False
    uppers = False

    for s in str_list:
        if s.isalnum():
            alphan = True
        if s.isalpha():
            alphabets = True
        if s.isdigit():
            digits = True
        if s.islower():
            lowers = True
        if s.isupper():
            uppers = True

    print(alphan)
    print(alphabets)
    print(digits)
    print(lowers)
    print(uppers)


if __name__ == "__main__":
    inp = input("Please provide string: \n")
    check_condition(inp)
