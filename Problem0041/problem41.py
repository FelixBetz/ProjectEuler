"""
Problem 41 https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital 
if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""


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


def generate_permutations(arr, current=[], result=[], used=None):
    """generate permutations"""
    if used is None:
        used = [False] * len(arr)

    if len(current) == len(arr):
        result.append(current[:])

    for i, _ in enumerate(arr):
        if used[i]:
            continue

        if i > 0 and arr[i] == arr[i - 1] and not used[i - 1]:
            continue

        used[i] = True
        generate_permutations(arr, current + [arr[i]], result, used)
        used[i] = False

    return result


def solve_problem41():
    """solve problem 41"""
    pandigital_numbers = []
    tmp_str = ""
    for i in range(1, 10):
        tmp_str += str(i)

        arr = generate_permutations(tmp_str)
        arr = [int("".join(num)) for num in arr]

        pandigital_numbers += arr

    pandigital_numbers.sort(reverse=True)

    for num in pandigital_numbers:
        if is_prime_number(num):
            return num
    return -1


print("value:", solve_problem41())
