#!/usr/bin/python3
for tens_digit in range(9):
    for ones_digit in range(tens_digit + 1, 10):
        print("{:d}{:d}, ".format(tens_digit, ones_digit), end="")
