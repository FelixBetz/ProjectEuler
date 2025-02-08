"""
Problem 43 https://projecteuler.net/problem=43

The number, 1406357289, is a 0 to 9 pandigital number because
it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
- d2d3d4=406 is divisible by 2
- d3d4d5=063 is divisible by 3
- d4d5d6=635 is divisible by 5
- d5d6d7=357 is divisible by 7
- d6d7d8=572 is divisible by 11
- d7d8d9=728 is divisible by 13
- d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations


def has_sub_str_property(arg_num):
    """check if given number has substring property"""
    divisors = [2, 3, 5, 7, 11, 13, 17]

    num_str = str(arg_num)

    idx = 1
    for divisor in divisors:
        if int(num_str[idx : idx + 3]) % divisor != 0:
            return False
        idx += 1

    return True


def solve_problem43():
    """solve problem 43"""
    pandigital_numbers = pandigital_numbers = [
        "".join(p) for p in permutations("0123456789")
    ]
    pandigital_numbers = [int(num) for num in pandigital_numbers]

    ret_sum = 0
    for num in pandigital_numbers:
        if has_sub_str_property(num):
            ret_sum += num

    return ret_sum


print("value:", solve_problem43())
