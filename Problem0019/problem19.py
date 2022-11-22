"""
Problem 19: https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

-   1 Jan 1900 was a Monday.
-   Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
-   A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_per_month_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(arg_year):
    """check if given year is a leap year"""
    if arg_year % 400 == 0:
        return True
    if arg_year % 100 == 0:
        return False
    if arg_year % 4 == 0:
        return True
    return False


def get_next_day(arg_day):
    """get next day"""
    arg_day += 1
    if arg_day > 6:
        arg_day = 0
    return arg_day


def solve_problem19():
    """solve problem 19"""
    cnt_mondays = 0
    weekday = 1  # 0=Monday, 1=Tuesday,...
    for year in range(1901, 2001):
        if is_leap_year(year):
            months = days_per_month_leap_year
        else:
            months = days_per_month
        for days in months:
            for i in range(days):
                # i ==1 (first of month) and weekday==6 (Sunday)
                if i == 0 and weekday == 6:
                    cnt_mondays += 1
                weekday = get_next_day(weekday)

    return cnt_mondays


print("How many Sundays fell on the first of the month " +
      "during the 20th century:", solve_problem19())
