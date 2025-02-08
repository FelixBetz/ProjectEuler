"""
Problem 32 https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use
of all the digits 1 to n exactly once; for example,
 the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
 identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way
so be sure to only include it once in your sum.
"""


def is_pan_digital(arg_str):
    """Check if the string is 1 to 9 pandigital"""
    arg_str = str(arg_str)
    if len(arg_str) != 9:
        return False

    # Check if the length of the array is 9
    digits = [int(digit) for digit in arg_str]
    digits.sort()

    # Check if all numbers from 1 to 9 are present exactly once
    for i in range(1, 10):
        if digits[i - 1] != i:
            return False

    return True


MAX_NUM = 9999


def solve_problem32():
    """solve problem 32"""
    unique_products = set()
    for a in range(1, MAX_NUM):
        for b in range(a, MAX_NUM):

            product = a * b
            loc_str = str(a) + str(b) + str(product)
            if is_pan_digital(loc_str):
                unique_products.add(product)
            if len(loc_str) > 9:
                break

    return sum(unique_products)


print("sum of all products :", solve_problem32())
