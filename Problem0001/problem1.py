"""
Problem 1: https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solve_problem1():
    """solve problem 1"""
    multiples_3_5 = set()

    # add multiples of 3
    for i in range(3, 1000, 3):
        multiples_3_5.add(i)

    # add multiples of 5
    for i in range(5, 1000, 5):
        multiples_3_5.add(i)

    # calculate multiple sum
    multiples_sum = 0
    for multiple in multiples_3_5:
        multiples_sum += multiple
    return multiples_sum


print(solve_problem1())
