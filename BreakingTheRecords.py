#Breaking the Records
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    tallymin = 0
    tallymax = 0
    seenscores = []
    seenscores.append(scores[0])
    for v in scores:
        if v > max(seenscores):
            tallymax += 1
            seenscores.append(v)
        elif v < min(seenscores):
            tallymin += 1
            seenscores.append(v)
    return(tallymax, tallymin)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
