"""
Problem 31 https://projecteuler.net/problem=31

In the United Kingdom the currency is made up of pound (£) and pence (p).
 There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def rec(value, largest_coin):
    """calc coins sequence recursively """
    if value == 200:
        return 1
    if value > 200:
        return 0
    ret = 0
    for coin in COINS:
        if coin <= largest_coin and coin <= 200 - value:
            ret += rec(value+coin, coin)
    return ret


def solve_problem31():
    """solve problem 31"""
    return rec(0, max(COINS))


print("distinct terms for a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100? :",
      solve_problem31())
