"""
Problem 26: https://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part.
"""


def get_recurring_cylce_len(arg_num):
    """returns recurring cycle in its decimal fraction part"""

    numerator = 1
    remainders = []
    while True:
        remainder = numerator % arg_num
        if remainder in remainders:
            break
        remainders.append(remainder)
        numerator = remainder * 10
        numerator %= arg_num
    return len(remainders)


def solve_problem26():
    """solve problem 26"""
    max_len = 0
    for i in range(1, 1001):
        max_len = max(max_len, get_recurring_cylce_len(i))
    return max_len


print("longest recurring cycle in its decimal fraction part:", solve_problem26())
