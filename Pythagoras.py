import math
import snake


def sqrt(x):
    return math.sqrt(x)


def pythag(mappings):
    l = len(mappings)
    z = int((l - 1)/2)
    if mappings[z] == mappings[z - 1] + mappings[z - 2]:
        if mappings[z - 1] == mappings[z - 2] + mappings[z - 3]:
            a = mappings[z - 3]
            b = mappings[z - 2]
            c = mappings[z - 1]
            d = mappings[z]
        else:
            a = mappings[z - 4]
            b = mappings[z - 2]
            c = mappings[z - 1]
            d = mappings[z]
    else:
        a = mappings[z - 2]
        b = mappings[z - 3]
        c = mappings[z - 1]
        d = mappings[z]
    m = sqrt(pow(a*d, 2) + pow(2*b*c, 2))
    return m
