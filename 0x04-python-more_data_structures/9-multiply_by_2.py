#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    temp_dictionary = a_dictionary.copy()
    for i in temp_dictionary.keys():
        temp_dictionary[i] *= 2
    return temp_dictionary
