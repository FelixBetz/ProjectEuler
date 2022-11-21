"""
Problem 9: https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solve_problem9():
    """solve problem 9"""
    num_c = 0
    cnt = 2

    # Limiting c would limit
    # all a, b and c
    product = 0
    while product == 0:

        # Now loop on n from 1 to m-1
        for i in range(1, cnt):
            num_a = cnt * cnt - i * i
            num_b = 2 * cnt * i
            num_c = cnt * cnt + i * i

            # if a+b+c==1000 break it
            if num_a+num_b+num_c == 1000:
                product = num_a*num_b*num_c
                break

        cnt += 1

    return product


print("product:", solve_problem9())
