"""
Problem 16: https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""


def get_digit_sum(arg_num):
    """returns digit sum of a given number"""
    digit_sum = 0
    while arg_num > 0:
        digit_sum += arg_num % 10
        arg_num //= 10
    return digit_sum


def solve_problem15():
    """solve problem 15"""
    value = 2 ** 1000
    return get_digit_sum(value)


print("sum of all the primes below two million:", solve_problem15())
