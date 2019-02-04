# ! /usr/bin/env python
# -*- coding: utf-8 -*-

from parts import get_first_part, get_second_part, get_rating_file
import requests
from bs4 import BeautifulSoup
import datetime
import re


def get_names_file():
    return 'F:\\Users\\Alena\\Documents\\New_folder\\ikt\\names.html'


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
    return words[0] + " " + words[1][0] + "."


def get_dates_and_names_arrays(array):
    temp_row_names = []
    dates_array = []
    names_list = []
    for name_or_date in array:
        date = is_it_date(name_or_date)
        if not date:
            if name_or_date != "":
                temp_row_names.append(name_or_date)
        else:
            if len(temp_row_names) > 0:
                names_list.append(temp_row_names)
                temp_row_names = []
            dates_array.append(date)
    if len(temp_row_names) > 0:
        names_list.append(temp_row_names)
    return dates_array, names_list


def make_data_array():
    array = read_old_data_from_file()

    dates_array, names_list = get_dates_and_names_arrays(array)  # just list of dates and names from file
    temp = []
    for raw in names_list:
        temp += raw
    uniq_names = list(dict.fromkeys(temp))

    names_and_places_array = {}   # list with places of every person per name
    # creates columns in result array
    if len(names_list[0]) > 0:
        for raw_counter, raw in enumerate(names_list):
            for name_counter, name in enumerate(raw):
                name_counter += 1
                try:
                    names_and_places_array[name].append(name_counter)
                except KeyError:
                    names_and_places_array[name] = []
                    names_and_places_array[name].append(name_counter)

            for name in uniq_names:
                try:
                    if len(names_and_places_array[name]) < raw_counter + 1:
                        names_and_places_array[name].append(52)
                except KeyError:
                    names_and_places_array[name] = []
                    names_and_places_array[name].append(52)

    return names_and_places_array, dates_array


def write_result(result):
    first_part = get_first_part()
    second_part = get_second_part()
    file = get_rating_file()
    with open(file, "w", encoding="utf-8") as file:
        file.write(first_part+result+second_part)


def make_result_string(names_and_places_array, dates_array):
    names_array = list(names_and_places_array.keys())
    names_array.sort()
    result = "var names_raw = ['place'"
    for key in names_array:
        result += ", '{}'".format(crop(key))

    result += "]\n var array = [names_raw \n"

    for ind, date in enumerate(dates_array):
        result += ", ['{}'".format(date.strftime("%d.%m"))
        for name in names_array:
            place = names_and_places_array[name][ind]
            result += ", " + str(place)
        result += "] \n"
    result += "];"

    return result


def get_new_data_from_site(old_array):
    url = get_url_to_parse()
    r = requests.get(url)
    text = r.text.encode("ISO-8859-1")   # text - bytes
    soup = BeautifulSoup(text, "lxml")
    film_list = soup.find('table', {'class': 'table-rating'})
    name_class = {}
    position_name = {}
    raws = film_list.find_all('tr')
    for x in raws:
        it = x.find_all('td')
        if len(it) > 3:
            name_class[it[1].text] = re.findall(r'\d+', it[3].text)[0]
            position_name[int(it[0].text)] = it[1].text

    new_data = []
    is_there_somethig_new = False
    for number in position_name:
        name = position_name[number]
        new_data.append(str(name))

    new_data.reverse()

    lenght = len(old_array) - 1
    if lenght > 6:
        for counter, el in enumerate(new_data):
            if el.strip() != old_array[lenght - counter].strip():
                is_there_somethig_new = True
    else:
        is_there_somethig_new = True

    if is_there_somethig_new:
        new_data.reverse()
        return new_data
    else:
        return None


def read_old_data_from_file():
    old_array = []
    file = get_names_file()
    with open(file, encoding="utf-8") as f:
        old_array = [row.strip() for row in f]
    return old_array


def write_new_data_in_file(new_data):
    file = get_names_file()
    with open(file, 'a', encoding="utf8") as output_file:
        output_file.write(str(datetime.datetime.today()) + "\n")
        for el in new_data:
            output_file.write(el + "\n")


