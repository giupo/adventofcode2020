#!/usr/bin/env python


import fileinput

def get_numbers():
    """
    get the numbers from advent of code
    """
    return [int(line) for line in fileinput.input()]

numbers = get_numbers()

def find_pair(numbers = get_numbers()):
    for x in numbers:
        for y in numbers:
            if x + y == 2020:
                return (x, y)

    return None


def find_triple(numbers = get_numbers()):
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x + y + z == 2020:
                    return (x, y, z)

    return None


x, y = find_pair(numbers)
print(x * y)
x, y, z = find_triple(numbers)
print(x * y * z)
