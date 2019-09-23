#Sock Merchant
#https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    tmp = []
    tally = 0
    for i in range(0,101):
        tmp.append(ar.count(i))
    for x in tmp:
        if x%2 == 0:
            tally += x//2
        else:
            tally += (x-1)//2
    return(tally)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
