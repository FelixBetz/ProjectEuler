"""
Problem 4: https://projecteuler.net/problem=4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def are_chars_equal(arg_str, arg_a, arg_b):
    """are 2 given indezies in string are equal"""
    return arg_str[arg_a] == arg_str[arg_b]


def is_palindrom(arg_num):
    """check if given number is a palindrom"""
    palindrom_str = str(arg_num)
    if len(palindrom_str) != 6:
        return False
    return are_chars_equal(palindrom_str, 0, 5) and \
        are_chars_equal(palindrom_str, 1, 4) and \
        are_chars_equal(palindrom_str, 2, 3)


def solve_problem4():
    """solve problem 4"""
    palindroms = []
    for i in range(100, 1000):
        for k in range(100, 1000):
            product = i*k
            if is_palindrom(product):
                palindroms.append(product)
    if len(palindroms) == 0:
        return 0
    return max(palindroms)


print("largest palindrom:", solve_problem4())
