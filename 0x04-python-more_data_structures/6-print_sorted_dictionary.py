#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    series_list = list(a_dictionary.keys())
    series_list.sort()
    for i in series_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
