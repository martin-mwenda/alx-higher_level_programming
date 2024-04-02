#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    i = 0
    if list_length <= 0:
        print("out of range")
        return cur_list
    while i < list_length:
        try:
            cur_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            cur_list.append(0)
        except TypeError:
            print("wrong type")
            cur_list.append(0)
        except IndexError:
            print("out of range")
            cur_list.append(0)
        finally:
            i += 1
    return cur_list
