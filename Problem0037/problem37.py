"""
Problem 37 https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


def get_number_digits(arg_number):
    """get digit array of given number"""
    digits = []
    while arg_number != 0:
        digits.append(arg_number % 10)
        arg_number //= 10
    digits.reverse()

    return digits


def is_prime_number(arg_num):
    """check if given number is a prime number"""
    if arg_num <= 3:
        return arg_num > 1
    if arg_num % 2 == 0 or arg_num % 3 == 0:
        return False
    limit = int(arg_num**0.5)
    for i in range(5, limit + 1, 6):
        if arg_num % i == 0 or arg_num % (i + 2) == 0:
            return False
    return True


def solve_problem37():
    """solve problem 37"""

    ret = []
    i = 10
    while len(ret) < 11:
        is_trunc_prime = True

        number = i
        # from left to right
        digits_left = get_number_digits(number)
        for idx, digit in enumerate(digits_left):
            if not is_prime_number(number):
                is_trunc_prime = False
                break
            minus = digit * 10 ** (len(digits_left) - idx - 1)
            number -= minus

        # from right to left
        number = i
        digits_right = get_number_digits(number)
        digits_right.reverse()

        for idx, digit in enumerate(digits_right):
            if not is_prime_number(number):
                is_trunc_prime = False
                break
            minus = digit * 10 ** (len(digits_right) - idx - 1)
            number -= digit
            number //= 10
        if is_trunc_prime:
            ret.append(i)
        i += 1

    return sum(ret)


print("sum of Truncatable Primes:", solve_problem37())
