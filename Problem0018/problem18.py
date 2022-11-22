"""
Problem 18: https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.
           3
          7 4
         2 4 6
        8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""

TRIANGLE_INPUT = [
    [3],
    [7,  5],
    [2,  4,  6],
    [8,  5,  9,  3],
]

TRIANGLE_INPUT = [
    ["75"],
    ["95", "64"],
    ["17", "47", "82"],
    ["18", "35", "87", "10"],
    ["20", "04", "82", "47", "65"],
    ["19", "01", "23", "75", "03", "34"],
    ["88", "02", "77", "73", "07", "63", "67"],
    ["99", "65", "04", "28", "06", "16", "70", "92"],
    ["41", "41", "26", "56", "83", "40", "80", "70", "33"],
    ["41", "48", "72", "33", "47", "32", "37", "16", "94", "29"],
    ["53", "71", "44", "65", "25", "43", "91", "52", "97", "51", "14"],
    ["70", "11", "33", "28", "77", "73", "17", "78", "39", "68", "17", "57"],
    ["91", "71", "52", "38", "17", "14", "91", "43", "58", "50", "27", "29", "48"],
    ["63", "66", "04", "68", "89", "53", "67",
        "30", "73", "16", "69", "87", "40", "31"],
    ["04", "62", "98", "27", "23", "09", "70", "98",
        "73", "93", "38", "53", "60", "04", "23"],



]

MAX_Y = len(TRIANGLE_INPUT)


def transform_triangle(arg_input):
    """transform triangle"""
    max_len = len(arg_input[-1]) * 2 - 1
    ret = []
    for row_idx, row in enumerate(arg_input):
        ret_row = [""]*max_len
        for col_index, col in enumerate(row):
            idx = 3 - row_idx+2*col_index
            ret_row[idx] = int(col)
        ret.append(ret_row)
    return ret


def print_triangle(arg_input):
    """print triangle to console"""
    for row in arg_input:
        row_str = ""
        for col in row:
            if col == "":
                row_str += "\t"
            else:
                row_str += "\t"+str(col)
        print(row_str)


def move(arg_input, arg_x, arg_y, arg_acc, arg_str):
    """move through triangle"""
    max_x = len(arg_input[0])
    max_y = len(arg_input)
    if arg_x < 0 or arg_x >= max_x:
        arg_str += str(arg_acc)
        # print(arg_str)
        return [arg_acc]
    if arg_y < 0 or arg_y >= max_y:
        arg_str += str(arg_acc)
        # print(arg_str)
        return [arg_acc]
    arg_str += str(arg_input[arg_y][arg_x])+"\t->\t"
    arg_acc += arg_input[arg_y][arg_x]
    return [] + \
        move(arg_input, arg_x - 1, arg_y + 1, arg_acc, arg_str) +\
        move(arg_input, arg_x + 1, arg_y + 1, arg_acc, arg_str)


def solve_problem18():
    """solve problem 18"""
    triangle = transform_triangle(TRIANGLE_INPUT)
    # print_triangle(triangle)
    rets = move(triangle, 3, 0, 0, "")
    return max(rets)


print("sum of all the primes below two million:", solve_problem18())
