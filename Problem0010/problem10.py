"""
Problem 10: https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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


def solve_problem10():
    """solve problem 10"""
    prime_sum = 0
    for i in range(2000000):
        if is_prime_number(i):
            prime_sum += i

    return prime_sum


print("sum of all the primes below two million:", solve_problem10())
