"""generate README.md file"""

import pandas as pd

# download from https://projecteuler.net/minimal=problems
CSV_PATH = "problems.txt"
README_PATH = "README.md"


IDX_SOLVE_STATUS = "Solve Status"
IDX_PROBLEM_ID = "ID"
IDX_TITLE = "Title"


def get_progress_bar_str(arg_percent):
    """Return progress bar string"""

    bar_chars = 50
    arg_percent = max(0, min(100, arg_percent))

    loads_chars = int(round(arg_percent * bar_chars / 100, 0))

    return "█" * loads_chars + "░" * (bar_chars - loads_chars) + "\n"


def generate_readme(arg_filename):
    """Generate README file"""

    problems = pd.read_csv(CSV_PATH, sep="##", engine="python")

    num_solved_problems = problems[IDX_SOLVE_STATUS].sum()
    solved_percentage = 100 * num_solved_problems / len(problems)

    lines = [
        "# Project Euler solutions",
        "This repository contains my solutions for "
        "[projecteuler.net](https://projecteuler.net).",
        "## What is Project Euler",
        '> "Project Euler exists to encourage, challenge,'
        " and develop the skills and enjoyment of anyone with an interest"
        ' in the fascinating world of mathematics."',
        "",
        "## My Progress",
        "",
        f"I solved `{num_solved_problems}` out of `{len(problems)}` problems!  ",
        "",
        get_progress_bar_str(solved_percentage) + f"{round(solved_percentage, 1)}%",
        "",
        "## Progress Overview",
        "Nr | Name | Solved",
        "--- | --- | ---",
    ]

    for _, problem in problems.iterrows():
        is_solved = "[x]" if problem[IDX_SOLVE_STATUS] == 1 else "[ ]"
        cnt = problem[IDX_PROBLEM_ID]
        name = problem[IDX_TITLE]
        str_name = f"[{name}](https://projecteuler.net/problem={cnt})"
        lines.append(f"{cnt} | {str_name} | {is_solved}")

    with open(arg_filename, "w+", encoding="utf-8") as file:
        file.writelines([line + "\n" for line in lines])


generate_readme(README_PATH)
