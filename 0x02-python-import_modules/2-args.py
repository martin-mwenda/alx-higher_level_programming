#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} argument".format(len(argv) - 1), end="")

    # no args
    if len(argv) == 1:
        print("s.")
    # we have more than 1 args
    elif len(argv) > 2:
        print("s:")
    # only one arg
    else:
        print(":")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
