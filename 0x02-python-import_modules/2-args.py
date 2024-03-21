#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    inser = len(sys.argv) - 1
    if inser == 0:
        print("0 arguments.")
    elif inser == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(inser))
    for i in range(inser):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
