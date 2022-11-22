"""
Problem 17: https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
 how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
 115 (one hundred and fifteen) contains 20 letters.
  The use of "and" when writing out numbers is in compliance with British usage.
"""


def get_digit_one(arg_digit):
    """get digits word 1 to 9"""
    digit_names = ["zero", "one", "two", "three",
                   "four", "five", "six", "seven", "eight", "nine"]
    if arg_digit > 9:
        return ""
    return digit_names[arg_digit]


def get_10_to_19(arg_digit):
    """get 10 to 19 as words"""
    ten_to_19 = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                 "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if 10 <= arg_digit <= 19:
        return ten_to_19[arg_digit-10]

    return ""


def get_digit_houndres(arg_digit):
    """get digit houndres"""
    twenty_to_ninty = ["one hundred",   "two hundred", "three hundred",
                       "four hundred", "five hundred", "six hundred",
                       "seven hundred", "eight hundred", "nine hundred"]
    if 1 <= arg_digit <= 9:
        return twenty_to_ninty[arg_digit-1]
    return ""


def get_digit_tens(arg_digit):
    """returns digit tens"""
    twenty_to_ninty = ["twenty", "thirty",  "forty",
                       "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 2 >= arg_digit >= 9:
        return ""
    return twenty_to_ninty[arg_digit-2]


def get_tens_str(arg_digit):
    """returns tens str"""
    ret_str = ""
    if 19 < arg_digit < 100:
        ones_remainder = arg_digit % 10
        tens_str = get_digit_tens((arg_digit//10) % 10)
        if ones_remainder == 0:
            ret_str = tens_str
        else:
            one_str = get_digit_one(ones_remainder)
            ret_str = tens_str+"-"+one_str
    elif 9 < arg_digit < 20:
        ret_str = get_10_to_19(arg_digit)
    return ret_str


def get_digit_as_string(arg_num):
    """returns digit sum of a given number"""
    ret_str = ""
    if arg_num == 1000:
        ret_str = "one thousand"
    elif 100 <= arg_num <= 999:
        ones_remainder = arg_num % 10
        ret_str = get_digit_houndres((arg_num//100) % 10)
        if ((arg_num//10) % 10) != 0:
            ret_str += " and " + get_tens_str(arg_num % 100)
        elif ones_remainder != 0:
            ret_str += " and "+get_digit_one(ones_remainder)
    elif 10 <= arg_num <= 99:
        ret_str = get_tens_str(arg_num)
    elif 0 <= arg_num <= 9:
        ret_str = get_digit_one(arg_num % 10)
    return ret_str


def count_letters(arg_str):
    """counts the letters of a char"""
    return len(arg_str.replace(" ", "").replace("-", ""))


def solve_problem15():
    """solve problem 15"""
    char_sum = 0
    for i in range(1, 1001):
        char_sum += count_letters(get_digit_as_string(i))

    return char_sum


print("sum of all the primes below two million:", solve_problem15())
