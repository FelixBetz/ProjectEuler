"""
Problem 20: https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def calc_faculty(arg_n):
    """calculates faculty of a given number"""
    fact = 1
    for i in range(1, arg_n+1):
        fact = fact * i
    return fact


def get_digit_sum(arg_num):
    """returns digit sum of a given number"""
    digit_sum = 0
    while arg_num > 0:
        digit_sum += arg_num % 10
        arg_num //= 10
    return digit_sum


def solve_problem20():
    """solve problem 20"""
    return get_digit_sum(calc_faculty(100))


print("sum of the digits in the number 100!:", solve_problem20())
