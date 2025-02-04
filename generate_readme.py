"""generate README.md file"""

import csv

# download from https://projecteuler.net/minimal=problems;csv
CSV_PATH = "pe_minimal_problems.csv"

README_PATH = "README.md"

SOVLE_COL_TEXT = "Solve Status"


def parse_csv_file(arg_filename):
    """parse problems from csv file"""

    idx_solve_status = 0

    ret = []
    with open(arg_filename, newline="", encoding="utf-8") as csv_file:
        spamreader = csv.reader(csv_file, delimiter=",", quotechar="|", escapechar="\\")
        for i, row in enumerate(spamreader):
            if i == 0:
                for col in row:
                    if SOVLE_COL_TEXT in col:
                        idx_solve_status = row.index(col)
            if i > 0:
                cnt = row[0]
                name = row[1].replace('"', "")
                is_solved = row[idx_solve_status] == "1"
                ret.append({"cnt": cnt, "name": name, "isSolved": is_solved})
    return ret


def get_progress_bar_str(arg_percent):
    """return progress bar string"""

    BAR_CHARS = 50

    # min max to 0 100
    arg_percent = max(0, arg_percent)
    arg_percent = min(100, arg_percent)

    loads_chars = arg_percent * BAR_CHARS / 100
    loads_chars = int(round(loads_chars, 0))

    return loads_chars * "█" + (BAR_CHARS - loads_chars) * "░" + "\n"


def generate_readme(arg_filename):
    """generate README file"""

    problems = parse_csv_file(CSV_PATH)
    num_solved_problems = len(
        list(filter(lambda problem: problem["isSolved"], problems))
    )
    solved_percentage = 100 * num_solved_problems / len(problems)
    lines = []

    lines.append("# Project Euler solutions")
    lines.append(
        "This repository contains my solutions for "
        + "[projecteuler.net](https://projecteuler.net)."
    )
    lines.append("## What is Project Euler")
    lines.append(
        '> "Project Euler exists to encourage, challenge,'
        + " and develop the skills and enjoyment of anyone with an interest"
        + ' in the fascinating world of mathematics."'
    )
    lines.append("")
    lines.append("## My Progress")
    lines.append("")
    lines.append(
        "I sloved `"
        + str(num_solved_problems)
        + "` out of `"
        + str(len(problems))
        + "` problems!  "
    )
    lines.append("")
    lines.append(
        get_progress_bar_str(solved_percentage) + str(round(solved_percentage, 1)) + "%"
    )
    lines.append("")
    lines.append("## Progress Overview")
    lines.append("Nr | Name | Solved")
    lines.append("--- | --- | ---")

    for problem in problems:
        if problem["isSolved"]:
            is_solved = "[x]"
        else:
            is_solved = "[ ]"
        cnt = problem["cnt"]
        name = problem["name"]
        str_name = "[" + name + "](https://projecteuler.net/problem=" + cnt + ")"

        lines.append(cnt + " | " + str_name + " | " + is_solved)

    for i, _ in enumerate(lines):
        lines[i] += "\n"

    with open(arg_filename, "w+", encoding="utf-8") as file:
        file.writelines(lines)


generate_readme(README_PATH)
