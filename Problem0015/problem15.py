"""
Problem 15: https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

import math

GRID_SIZE = 20


def solve_problem15():
    """solve problem 15"""
    return math.comb(2 * GRID_SIZE, GRID_SIZE)


print("sum of all the primes below two million:", solve_problem15())
