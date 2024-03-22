#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    gross = 0
    for number in my_list:
        if number not in new_list:
            gross += number
            new_list.append(number)
    return gross
