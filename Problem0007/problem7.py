"""
Problem 7: https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime_number(arg_num):
    """check if given number is a prime number"""
    if arg_num <= 3:
        return arg_num > 1
    if arg_num % 2 == 0 or arg_num % 3 == 0:
        return False
    limit = int(arg_num**0.5)
    for i in range(5, limit+1, 6):
        if arg_num % i == 0 or arg_num % (i+2) == 0:
            return False
    return True


def solve_problem7():
    """solve problem 7"""
    cnt = 0
    num = 1
    while True:
        if is_prime_number(num):
            cnt += 1
            if cnt >= 10001:
                break

        num += 1
    return num


print("10001st prime number:", solve_problem7())
