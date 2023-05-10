#!/usr/bin/python3
for alpha in reversed(range(97, 123)):
    if alpha % 2 == 0:
        print('{}'.format(chr(alpha)), end="")
    else:
        print('{}'.format(chr(alpha - 32)), end="")
