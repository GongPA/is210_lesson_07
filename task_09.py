#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Task 09 """

import task_09_utility

DATA_FILES = [
    {'data': 'task_09_data/router_01.csv'},
    {'data': 'task_09_data/router_02.csv'},
    {'data': 'task_09_data/router_03.csv'},
]


def load_data(data):
    """ accepts DATA_FILES and returns a dictionary """

    counter = 1
    data_dict = {}

    for item in data:
        #in the loop task_09_utility.get_data() function and passing
        #it the file path associated with the data key of your loop value.
        log_in_csv = task_09_utility.get_data(item['data'])
        data_dict[counter] = log_in_csv
        counter += 1
    return data_dict


def merge_data(dict_object):
    """
        accepts dict_object from function "load_data()"
        returns a list
    """

    dict_merge = {}

    for key_in_log, router in dict_object.iteritems():
        # This loop is sprightful just follow the instruction step by step
        for dicts in router:

            for clock, avg in dicts.iteritems():

                clock = dicts['clock']
                avg = dicts['value_avg']

                if clock is None:
                    clock = 0
                    day_time_key = 0
                else:
                    day_time_key = int(clock[8:13])

                if day_time_key in dict_merge:
                    dict_merge[day_time_key][key_in_log] = avg
                else:
                    dict_merge[day_time_key] = [clock, 0, 0, 0]
                    dict_merge[day_time_key][key_in_log] = avg

    return task_09_utility.sort_dict(dict_merge)
