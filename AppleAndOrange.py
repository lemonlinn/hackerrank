# Apple and Orange
# https://www.hackerrank.com/challenges/apple-and-orange/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    stapple = [(ap + a) for ap in apples]
    storange = [(o + b) for o in oranges]
    atally = 0
    otally = 0
    for x in stapple:
        if x in range(s, t+1):
            atally += 1
    for y in storange:
        if y in range(s, t+1):
            otally += 1
    print(atally)
    print(otally)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
