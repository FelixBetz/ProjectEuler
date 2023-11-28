"""
Problem 34 https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 2 + 24 + 120 = 145

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

import itertools


def get_number_digits(arg_number):
    """get digit array of given number"""
    digits = []
    while arg_number != 0:
        digits.append(arg_number % 10)
        arg_number //= 10
    digits.reverse()

    return digits


def is_prime_number(arg_num):
    """check if given number is a prime number"""
    if arg_num <= 3:
        return arg_num > 1
    if arg_num % 2 == 0 or arg_num % 3 == 0:
        return False
    limit = int(arg_num**0.5)
    for i in range(5, limit + 1, 6):
        if arg_num % i == 0 or arg_num % (i + 2) == 0:
            return False
    return True


def rotate_array_right(arr):
    rotated_arr = arr[-1:] + arr[:-1]
    return rotated_arr


def solve_problem35():
    """solve problem 34"""

    # build faculty array
    faculty_array = []
    for i in range(1_000_000):
        if is_prime_number(i):
            digits = get_number_digits(i)
            numbers = []
            for _ in range(len(digits)):
                numbers.append(int("".join(map(str, digits))))
                digits = rotate_array_right(digits)

            is_cicular_prime = True
            for num in numbers:
                if not is_prime_number(num):
                    is_cicular_prime = False
                    break
            if is_cicular_prime:
                faculty_array.append(i)

    return len(faculty_array)


print("sum of the courios numbers:", solve_problem35())
