"""
Problem 21: https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def calc_amicable_number(arg_num):
    """calculates amicalbe number"""
    divisors = []
    for i in range(1, arg_num//2 + 1):
        if arg_num % i == 0:
            divisors.append(i)
    return sum(divisors)


def is_amicalbe_pair(arg_a):
    """check if is amicable pair"""
    loc_b = calc_amicable_number(arg_a)
    loc_c = calc_amicable_number(loc_b)
    return arg_a != loc_b and arg_a == loc_c


def solve_problem21():
    """solve problem 21"""
    amicable_sum = 0
    for i in range(10000):
        if is_amicalbe_pair(i):
            amicable_sum += i
    return amicable_sum


print("sum of all the amicable numbers under 10000:", solve_problem21())
