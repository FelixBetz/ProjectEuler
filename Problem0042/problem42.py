"""
Problem 42 https://projecteuler.net/problem=42

The nth term of the sequence of triangle numbers is given by, t_n = 1/2 * n * (n + 1); 
so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are 
triangle words?
"""


def generate_triangle_numbers(arg_amount=100000):
    """generate triangle numbers"""
    triangle_numbers = []

    for i in range(1, arg_amount):
        triangle_numbers.append(int(0.5 * i * (i + 1)))

    return triangle_numbers


def calc_word_value(arg_word):
    """calc word value"""
    arg_word = arg_word.replace('"', "")
    arg_word = arg_word.strip()
    loc_sum = 0
    for char in arg_word:

        ordinary = ord(char.lower()) - ord("a") + 1
        loc_sum += ordinary

    return loc_sum


def solve_problem42():
    """solve problem 42"""
    triangle_numbers = generate_triangle_numbers(100000)
    ret_cnt = 0
    with open("0042_words.txt", encoding="utf-8") as file:
        words = []
        for line in file:
            words += line.split(",")

        for word in words:
            if calc_word_value(word) in triangle_numbers:
                ret_cnt += 1
    return ret_cnt


print("number of triangle words:", solve_problem42())
