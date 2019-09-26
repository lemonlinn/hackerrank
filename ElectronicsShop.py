#Electronics Shop
#https://www.hackerrank.com/challenges/electronics-shop/problem

#Here's some code that did the job but was crazy inefficient, and got me timed out:

#def getMoneySpent(keyboards, drives, b):
    #keyboards.sort(reverse=True)
    #drives.sort()
    #ans = -1
    #newj = 0
    #for i in range(0, len(keyboards)):
        #for j in range(newj, len(drives)):
            #if min(keyboards) + min(drives) > b:
                #break
            #elif keyboards[i] + drives[j] > ans and keyboards[i] + drives[j] <= b:
                #ans = keyboards[i] + drives[j]
                #newj = j
    #return(ans)

#Here's my final submission:

#!/bin/python3

import os
import sys

def getMoneySpent(keyboards, drives, b):
    ans = -1
    for x in keyboards:
        for y in drives:
            if x+y <= b:
                ans = max(ans,(x+y))
    return(ans)

#by functionally replacing the elif statement from before with max(), things immediately cleaned up
