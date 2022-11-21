"""
Problem 3: https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def solve_problem3():
    """solve problem 3"""
    num = 600851475143
    prime_number = 2
    while num >= prime_number*prime_number:
        if num % prime_number == 0:
            num = num // prime_number
        else:
            prime_number += 1
    return num


print("largest prime factor:", solve_problem3())
