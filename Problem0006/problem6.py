"""
Problem 6: https://projecteuler.net/problem=6
The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
"""


def solve_problem6():
    """solve problem 6"""
    onehundred_nums = range(1, 101)
    sum_squares = 0
    for i in onehundred_nums:
        sum_squares += i**2

    return sum(onehundred_nums)**2 - sum_squares


print("difference:", solve_problem6())
