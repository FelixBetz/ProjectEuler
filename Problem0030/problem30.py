"""
Problem 30 https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def get_number_digits(arg_number):
    """get digit array of given number"""
    digits = []
    while arg_number != 0:
        digits.append(arg_number % 10)
        arg_number //= 10
    return digits


def solve_problem30():
    """solve problem 30"""
    ret = []
    for i in range(2, 1000000):
        sum_powers = 0
        for digit in get_number_digits(i):
            sum_powers += digit**5
        if sum_powers == i:
            ret.append(i)
    return sum(ret)


print("distinct terms for a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100? :",
      solve_problem30())
