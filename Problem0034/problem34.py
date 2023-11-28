"""
Problem 34 https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 2 + 24 + 120 = 145

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""


def get_number_digits(arg_number):
    """get digit array of given number"""
    digits = []
    while arg_number != 0:
        digits.append(arg_number % 10)
        arg_number //= 10
    return digits


def calc_faculty(arg_n):
    """calculates faculty of a given number"""
    fact = 1
    for i in range(1, arg_n + 1):
        fact = fact * i
    return fact


def solve_problem34():
    """solve problem 34"""

    # build faculty array
    faculty_array = []
    for i in range(10):
        faculty_array.append(calc_faculty(i))

    digit_sum = 0
    for i in range(3, 100_000):
        digits = get_number_digits(i)
        if sum([faculty_array[digit] for digit in digits]) == i:
            digit_sum += i

    return digit_sum


print("sum of the courios numbers:", solve_problem34())
