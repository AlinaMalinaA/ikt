# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from processing_tools import *
from shutil import copyfile


old_data = read_old_data_from_file()
new_data = get_new_data_from_site(old_data)
if new_data:
    write_new_data_in_file(new_data)

    result_array, dates_array, names_array, control_names_list = make_data_array()
    result = make_result_string(result_array, dates_array, names_array, control_names_list)
    write_result(result)


copyfile("C:\\Users\\Alena\\Documents\\New folder\\index.html",
         "C:\\Users\\Alena\\Documents\\temp\\AlinaMalinaA.github.io\\index.html")
