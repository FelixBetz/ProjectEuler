"""
Problem 40 https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the n-th digit of the fractional part, find the value of the following expression:
d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
"""

MAX_DIGIT = 1000000


def create_fractional_part(arg_num_digits):
    """create fractional part"""
    fractional_part = ""
    i = 1
    while len(fractional_part) < arg_num_digits:
        fractional_part += str(i)
        i += 1
    return fractional_part


def d_th_digit(arg_digit, arg_fractional_part):
    """return d_th digit"""
    return int(arg_fractional_part[arg_digit - 1])


def solve_problem40():
    """solve problem 40"""
    decimal_fraction = create_fractional_part(MAX_DIGIT)

    loc_value = 1

    d = 1
    while d <= MAX_DIGIT:
        loc_value *= d_th_digit(d, decimal_fraction)
        d *= 10

    return loc_value


print("value:", solve_problem40())
