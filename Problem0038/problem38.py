"""
Problem 38 https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3).
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ..., n) where n > 1?
"""


def is_pan_digital(arg_str):
    """Check if the string is 1 to 9 pandigital"""
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


def get_pandigital_multiplies(arg_num, arg_mulitplies):
    """Get the pandigital multiplies of a number"""
    num_string = ""
    for i in range(arg_mulitplies):
        num_string += str(arg_num * (i + 1))
        if len(num_string) > 9:
            return ""

    return num_string


MAX_NUM = 9999


def solve_problem38():
    """solve problem 38"""

    max_num = 0
    for i in range(1, MAX_NUM):
        for n in range(2, 12):
            str_pandigital_mulitply = get_pandigital_multiplies(i, n)
            if is_pan_digital(str_pandigital_mulitply):
                pandigital_mulitply = int(str_pandigital_mulitply)
                max_num = max(max_num, pandigital_mulitply)

    return max_num


print("sum of Truncatable Primes:", solve_problem38())
