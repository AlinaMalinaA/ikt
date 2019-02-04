# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from processing_tools import *
from shutil import copyfile


old_data = read_old_data_from_file()
new_data, names_and_groups = get_new_data_from_site(old_data)
print("Пишем?", bool(new_data))
if new_data:
    write_new_data_in_file(new_data)

names_and_places_array, dates_array = make_data_array()
result = make_result_string(names_and_places_array, dates_array, names_and_groups)
write_result(result)


