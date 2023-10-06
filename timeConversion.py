#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    # Extract hours, minutes, and seconds from the input string
    hh = int(s[0:2])
    mm = int(s[3:5])
    ss = int(s[6:8])
    am_pm = s[8:10]

    # Check if it's PM and not 12 PM, then add 12 to hours
    if am_pm == 'PM' and hh != 12:
        hh += 12
    # If it's AM and 12 AM, set hours to 00
    elif am_pm == 'AM' and hh == 12:
        hh = 0

    # Convert hours, minutes, and seconds to strings and format them with leading zeros
    hh_str = str(hh).zfill(2)
    mm_str = str(mm).zfill(2)
    ss_str = str(ss).zfill(2)

    # Combine the formatted values to create the 24-hour time string
    military_time = f"{hh_str}:{mm_str}:{ss_str}"

    return military_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
