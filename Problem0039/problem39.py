"""
If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, 
there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?
"""

MAX_PERIMETER = 1000


def is_right_triangle(a, b, c):
    """check if the triangle is right"""
    return a**2 + b**2 == c**2


def solve_problem39():
    """solve problem 39"""

    solutions_p = [0] * (MAX_PERIMETER + 1)

    for a in range(1, MAX_PERIMETER):
        for b in range(a, MAX_PERIMETER):
            for c in range(b, MAX_PERIMETER):
                perimeter = a + b + c
                if perimeter > MAX_PERIMETER:
                    break
                if is_right_triangle(a, b, c):
                    solutions_p[perimeter] += 1

    max_index = max(range(len(solutions_p)), key=lambda i: solutions_p[i])

    return max_index


print("maximised solutions for p =", solve_problem39())
