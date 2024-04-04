#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z')+1)):
    if i % 2 == 1:
        i = chr(i - 32)
    else:
        i = chr(i)
    print("{}".format(i), end="")
