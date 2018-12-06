# ! /usr/bin/env python
# -*- coding: utf-8 -*-


def get_rating_file():
    return 'C:\\Users\\Alena\\Documents\\test_project\\new_try\\index.html'


def get_first_part():
    first = ""
    for row in rows:
        first += row
        if '<script type="text/javascript">' in row:
            break
    first += "var array = ["
    return first


def get_second_part():
    second = "];"
    start_write = False
    for row in rows:
        if 'var isSelected = false' in row:
            start_write = True
        if start_write:
            second += row
    return second


file = get_rating_file()
with open(file) as f:
    rows = f.readlines()

