"""
Problem 27: https://projecteuler.net/problem=27

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| <= 1000
where |n| ist modulus/absoulte value of n

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n, starting with  n=0.
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


def solve_problem27():
    """solve problem 27"""
    solution_a = 0
    solution_b = 0
    num_primes = 0
    for a in range(-999, 1000):
        for b in range(0, 1001):
            n = 0
            while True:
                #n^2 + an +b
                val = n**2 + a*n+b
                if not is_prime_number(val):
                    if n > num_primes:
                        solution_a = a
                        solution_b = b
                        num_primes = n
                    break
                n += 1

    return solution_a * solution_b


print("product of the coefficients, a and b:", solve_problem27())
