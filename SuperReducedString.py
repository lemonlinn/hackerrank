#!/bin/python3

# https://www.hackerrank.com/challenges/reduced-string/problem

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    slist = [l for l in s]
    try:
        for i in range(len(slist)-1):
            if slist[i] == slist[i+1]:
                del(slist[i:i+2])
    except:
        s = re.sub('[, ]+','',', '.join(slist))
        return(superReducedString(s))

    s = re.sub('[, ]+','',', '.join(slist))
    if s == "":
        return('Empty String')
    else:
        return(s)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
