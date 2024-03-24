#!/usr/bin/python3
def weight_average(input_list=[]):
    if not input_list:
        return 0

    numerator = 0
    denominator = 0

    for tup in input_list:
        numerator += tup[0] * tup[1]
        denominator += tup[1]

    return (numerator / denominator)
