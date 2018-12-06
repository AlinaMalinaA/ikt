# ! /usr/bin/env python
# -*- coding: utf-8 -*-

from parts import get_first_part, get_second_part, get_rating_file
import requests
from bs4 import BeautifulSoup
import datetime


def get_names_file():
    return 'C:\\Users\\Alena\\Documents\\test_project\\new_try\\names.html'


def get_url_to_parse():
    calendar_years = "2018/2019"
    faculty = "725"
    course = 4
    return 'https://de.ifmo.ru/?node=rating&app={0}&std&depId={1}&year={2}'.format(calendar_years, faculty, course)


def is_it_date(date):
    try:
        return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    except:
        return False


def crop(name):
    words = name.split(" ")
    return words[0]


def get_dates_and_names_arrays(array):
    temp_row_names = []
    dates_array = []
    names_list = []
    for name_or_date in array:
        date = is_it_date(name_or_date)
        if not date:
            temp_row_names.append(name_or_date)
        else:
            if len(temp_row_names) > 0:
                names_list.append(temp_row_names)
                temp_row_names = []
            dates_array.append(date)
    return dates_array, names_list


def make_data_array():
    array = read_old_data_from_file()

    dates_array, names_list = get_dates_and_names_arrays(array)

    names_and_places_array = {}
    names_array = []

    # creates columns in result array
    for counter, name in enumerate(names_list[0]):
        if name not in names_array:
            names_array.append(name)
        names_and_places_array[name] = []

    # fill person places in result array
    for number, row in enumerate(names_list):
        keys = names_and_places_array.keys()
        for counter,  name in enumerate(row):
            if name in names_and_places_array:
                names_and_places_array[name].append(counter+1)
                keys.remove(name)
            else:
                names_and_places_array[name] = [counter]
        for k in keys:
            names_and_places_array[k].append(52)

        for name in row:
            if len(names_and_places_array[name]) < number:
                names_and_places_array[name].append(51)

    return names_and_places_array, dates_array, names_array, names_list


def write_result(result):
    first_part = get_first_part()
    second_part = get_second_part()
    file = get_rating_file()
    with open(file, "w") as file:
        file.write(first_part+result+second_part)


def make_result_string(result_array, dates_array, names_array, control_names_list):
    result = "['place' "
    names_array.sort()
    keys = result_array.keys()
    for key in names_array:
        result += ",'{}'".format(crop(key))

    result += "]"

    for counter, row in enumerate(control_names_list):
        line = ",["
        line += "'{0}'".format(dates_array[counter].strftime("%d.%m.%Y"))
        for name in names_array:
            for key in keys:
                if key == name:
                    try:
                        line += ",{}".format(str(result_array[key][counter]))
                    except IndexError:
                        line += ",51"
        line += "]"
        result += line

    return result


def get_new_data_from_site(old_array):
    url = get_url_to_parse()
    r = requests.get(url)
    text = r.text.encode('ISO-8859-1')
    soup = BeautifulSoup(text, "lxml")
    film_list = soup.find('table', {'class': 'table-rating'})
    items = film_list.find_all('td')
    new_data = []
    is_the_same = False
    for counter, item in enumerate(items):
        if "344" not in item.text.encode('utf-8'):
            if 0 < counter % 4 < 2:
                new_data.append(item.text.encode('utf-8'))
    new_data.reverse()
    lenght = len(old_array) - 1
    if lenght > 5:
        for counter, el in enumerate(new_data):
            if el.strip() != old_array[lenght - counter].strip():
                is_the_same = True
    else:
        is_the_same = True
    if is_the_same:
        new_data.reverse()
        return new_data
    else:
        return None


def read_old_data_from_file():
    old_array = []
    file = get_names_file()
    try:
        with open(file) as f:
            old_array = [row.strip() for row in f]
    except:
        print "Can't open file", file
    return old_array


def write_new_data_in_file(new_data):
    file = get_names_file()
    with open(file, 'a') as output_file:
        output_file.write(str(datetime.datetime.today()) + "\n")
        for el in new_data:
            output_file.write(el + "\n")


