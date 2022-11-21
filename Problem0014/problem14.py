"""
Problem 14: https://projecteuler.net/problem=14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def calc_sequence(arg_starting_num):
    """returns the length of the chain"""
    sequence_len = 1
    while arg_starting_num != 1:
        if arg_starting_num % 2 == 0:
            arg_starting_num //= 2
        else:
            arg_starting_num = 3*arg_starting_num+1
        sequence_len += 1
    return sequence_len


def solve_problem14():
    """solve problem 14"""
    max_len = 0
    index = 0
    for i in range(1, 1000 * 1000):
        length = calc_sequence(i)
        if length > max_len:
            index = i
            max_len = length

    return index


print("sum of all the primes below two million:", solve_problem14())
