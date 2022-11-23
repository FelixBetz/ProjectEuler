"""
Problem 24: https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

permutations = []


def generate_ermutations(arg_list, size):
    """Generating permutation using Heap Algorithm"""
    # if size becomes 1 then prints the obtained
    # permutation
    if size == 1:
        permutations.append(arg_list.copy())
        return

    for i in range(size):
        generate_ermutations(arg_list, size-1)

        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size & 1:
            arg_list[0], arg_list[size-1] = arg_list[size-1], arg_list[0]
        else:
            arg_list[i], arg_list[size-1] = arg_list[size-1], arg_list[i]


def calc_weight(arg_list):
    """calc weight of a given list"""
    weight = 0
    for i, digit in enumerate(arg_list):
        factor = 10**(len(arg_list) - i)
        weight += digit * factor

    return weight


def solve_problem24():
    """solve problem 24"""

    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #values = [0, 1, 2]
    len_values = len(values)

    generate_ermutations(values, len_values)
    permutations.sort(key=calc_weight)

    one_millionth_permutation = permutations[1000*1000 - 1]
    ret_str = ""
    for digit in one_millionth_permutation:
        ret_str += str(digit)
    return ret_str


print("millionth lexicographic permutation of the digits 0 to 9:", solve_problem24())
