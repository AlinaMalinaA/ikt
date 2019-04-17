# ! /usr/bin/env python
# -*- coding: utf-8 -*-


def get_rating_file():
    return 'index.html'


def get_first_part():
    first = ""
    for row in rows:
        first += row
        if '<script type="text/javascript">' in row:
            break

    return first


def get_second_part():
    second = "\n"
    start_write = False
    for row in rows:
        if 'show_only = [];' in row:
            start_write = True
        if start_write:
            second += row
    return second


file = get_rating_file()
with open(file, encoding="utf-8") as f:
    rows = f.readlines()

