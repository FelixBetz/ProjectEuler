"""
Problem 33 https://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, 
as an inexperienced mathematician in attempting to simplify 
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""


def product_of_list(arg_list):
    """product of list"""
    ret = 1
    for i in arg_list:
        ret *= i
    return ret


def ggt(a, b):
    """greatest common divisor"""
    while b != 0:
        a, b = b, a % b
    return a


def solve_problem33():
    """solve problem 33"""
    numerators_product = 1
    denominators_product = 1
    for a in range(10, 100):
        for b in range(10, 100):
            if a / b < 1:
                for i in range(1, 10):
                    str_a = str(a)
                    str_b = str(b)

                    str_a = str_a.replace(str(i), "")
                    str_b = str_b.replace(str(i), "")

                    if len(str_a) == 1 and len(str_b) == 1:
                        aa = int(str_a)
                        bb = int(str_b)
                        if bb != 0:
                            if aa / bb == a / b:
                                numerators_product *= aa
                                denominators_product *= bb

    divsor = ggt(numerators_product, denominators_product)

    return denominators_product // divsor


print("sum of the courios numbers:", solve_problem33())
