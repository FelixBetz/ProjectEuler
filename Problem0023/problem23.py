"""
Problem 23: https://projecteuler.net/problem=23

A perfect number is a number for which the sum of
its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
 which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and
 it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though
it is known that the greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers
which cannot be written as the sum of two abundant numbers.
"""


def is_abundant(arg_num):
    """returns number of divsors for a given number"""
    divisor_sum = 0
    for i in range(1, arg_num//2 + 1):
        if arg_num % i == 0:
            divisor_sum += i
    return divisor_sum > arg_num


def solve_problem23():
    """solve problem 23"""

    abundant_numbers = []
    for i in range(1, 28124):
        if is_abundant(i):
            abundant_numbers.append(i)

    abundant_sums = set([])
    for i in abundant_numbers:
        for k in abundant_numbers:
            sum_ik = i+k
            if sum_ik <= 28123:
                abundant_sums.add(sum_ik)
            else:
                break
    abundant_sum = 0
    for i in range(28124):
        if i not in abundant_sums:
            abundant_sum += i

    return abundant_sum


print("sum of all the positive integers which cannot" +
      " be written as the sum of two abundant numbers:", solve_problem23())
