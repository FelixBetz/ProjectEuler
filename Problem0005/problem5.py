"""
Problem 5: https://projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def solve_problem5():
    """solve problem 5"""
    num = 20
    while True:
        is_devivisble = True
        # evenly divisible by all of the numbers from 1 to 20
        for i in range(1, 21):
            if num % i != 0:
                is_devivisble = False

        if is_devivisble:
            break

        # must be a multiple of 20
        num += 20

    return num


print("evenly divisible by all of the numbers from 1 to 20:", solve_problem5())
