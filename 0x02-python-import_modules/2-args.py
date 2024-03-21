#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    count = 1

    
    numargs = len(argv) - 1
    if numargs == 0:
        print(f"{numargs:d} arguments.")
    if numargs == 1:
        print(f"{numargs:d} argument:")
    if numargs > 1:
        print(f"{numargs:d} arguments:")
    while count < len(argv):
        print(f"{count:d}: {argv[count]}")
        count += 1
