#!/usr/bin/env python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print(char, end='')
    print(
