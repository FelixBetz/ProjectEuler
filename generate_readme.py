"""generate README.md file"""
import csv

# download from https://projecteuler.net/minimal=problems;csv
CSV_PATH = "pe_minimal_problems.csv"

README_PATH = "README.md"


def parse_csv_file(arg_filename):
    """parse problems from csv file"""
    ret = []
    with open(arg_filename, newline='', encoding="utf-8") as csv_file:
        spamreader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for i, row in enumerate(spamreader):
            if i > 0:
                cnt = row[0]
                name = row[1].replace("\"", "")
                is_solved = row[4] == "1"
                ret.append({"cnt": cnt, "name": name, "isSolved": is_solved})
    return ret


def generate_readme(arg_filename):
    """generate README file"""

    problems = parse_csv_file(CSV_PATH)
    num_solved_problems = len(
        list(filter(lambda problem: problem["isSolved"], problems)))
    solved_percentage = 100 * num_solved_problems // len(problems)
    lines = []

    lines.append("# Project Euler solutions")
    lines.append("This repository contains my solutions for" +
                 "[projecteuler.net](https://projecteuler.net).")
    lines.append("## What is Project Euler")
    lines.append("> \"Project Euler exists to encourage, challenge," +
                 " and develop the skills and enjoyment of anyone with an interest" +
                 " in the fascinating world of mathematics.\"")
    lines.append("")
    lines.append("## My Progress")
    lines.append("")
    lines.append("I sloved `" + str(num_solved_problems) +
                 "` out of `" + str(len(problems))+"` problems!  ")
    lines.append("")
    lines.append("!["+str(solved_percentage) +
                 "%](https://progress-bar.dev/"+str(solved_percentage)+"?width=500)")
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
        str_name = "["+name + "](https://projecteuler.net/problem="+cnt+")"

        lines.append(cnt+" | " + str_name + " | "+is_solved)

    for i, _ in enumerate(lines):
        lines[i] += "\n"

    with open(arg_filename, "w+", encoding="utf-8") as file:

        file.writelines(lines)


generate_readme(README_PATH)
