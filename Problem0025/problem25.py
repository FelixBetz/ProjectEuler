"""
Problem 25: https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def count_digits(arg_num):
    """returns the amount of digits for a given number"""
    cnt_digits = 0
    while arg_num > 0:
        arg_num //= 10
        cnt_digits += 1
    return cnt_digits


def solve_problem25():
    """solve problem 25"""
    num1 = 1
    num2 = 2
    cnt_index = 3

    while True:
        tmp = num1 + num2
        cnt_index += 1

        if count_digits(tmp) == 1000:
            return cnt_index
        num1 = num2
        num2 = tmp


print("index of the Fibonacci sequence to contain 1000 digits:", solve_problem25())
