#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ind = 0
    while True:
        try:
            if ind < x:
                print(my_list[ind], end='')
                ind += 1
            else:
                print()
                return ind
        except IndexError:
            print()
            return ind
