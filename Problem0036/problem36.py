"""
Problem 36 https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001b (binbary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10
 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def get_number_digits(arg_number):
    """get digit array of given number"""
    digits = []
    while arg_number != 0:
        digits.append(arg_number % 10)
        arg_number //= 10
    digits.reverse()

    return digits


def is_palindrom(arg_digits_array):
    length = len(arg_digits_array) // 2

    for i in range(length):
        f_el = arg_digits_array[i]
        l_el = arg_digits_array[len(arg_digits_array) - i - 1]
        if f_el != l_el:
            return False
    return True


def solve_problem36():
    """solve problem 36"""

    ret_sum = 0
    for i in range(1_000_000):
        digits_10 = get_number_digits(i)

        i_bin_str = bin(i)[2:]  # remove 0b from string
        digits_2 = [int(i) for i in i_bin_str]  # covnert string to number array

        if is_palindrom(digits_10) and is_palindrom(digits_2):
            ret_sum += i

    return ret_sum


print("sum of double-base palindromes:", solve_problem36())
