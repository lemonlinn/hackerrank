# Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    tmp = s.split(":")
    AMval = ["01","02","03","04","05","06","07","08","09","10","11"]
    PMval = ["13","14","15","16","17","18","19","20","21","22","23"]
    matchindex = 0
    if any("PM" in s for s in tmp) and any(word in tmp[0] for word in AMval):
        matchindex += AMval.index(tmp[0])
        return(PMval[matchindex] + ":" + tmp[-2] + ":" + tmp[-1].replace("PM",""))
    elif any("AM" in s for s in tmp) and "12" in tmp[0]:
        return("00" + ":" + tmp[-2] + ":" + tmp[-1].replace("AM",""))
    elif any("PM" in s for s in tmp) and "12" in tmp[0]:
        return("12" + ":" + tmp[-2] + ":" + tmp[-1].replace("PM",""))
    else:
        return(s.replace("AM",""))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
