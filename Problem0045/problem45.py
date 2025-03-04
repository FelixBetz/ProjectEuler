"""
Problem 45 https://projecteuler.net/problem=45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle: T_n = n(n + 1) / 2
1, 3, 6, 10, 15, ...

Pentagonal: P_n = n(3n - 1) / 2
1, 5, 12, 22, 35, ...

Hexagonal: H_n = n(2n - 1)
1, 6, 15, 28, 45, ...

It can be verified that T_285 = P_165 = H_143 = 40755.
Find the next triangle number that is also pentagonal and hexagonal.
"""

import math


def get_nth_triangle(n):
    """calculate the nth triangle number"""
    return int(n * (n + 1) * 0.5)


def is_pentagonal(n):
    """check if it is a pentagonal number"""
    return ((1 + math.sqrt(1 + 24 * n)) / 6).is_integer()


def is_hexagonal(n):
    """check if it is a pentagonal number"""
    return ((1 + math.sqrt(1 + 8 * n)) / 4).is_integer()


def solve_problem45():
    """solve problem 45"""
    n = 285 + 1
    while True:
        triangle_num = get_nth_triangle(n)
        if is_pentagonal(triangle_num) and is_hexagonal(triangle_num):
            return triangle_num
        n += 1


print("value:", solve_problem45())
