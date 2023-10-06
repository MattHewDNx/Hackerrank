

import math
import os
import random
import re
import sys



def plusMinus(arr):
    length = len(arr)

    zero =0
    minus =0
    plus =0

    for i in range(0,length):
        if arr[i]<0:
            minus+=1
        elif arr[i]>0:
            plus+=1
        
        else:
            zero+=1
    return[plus/length,minus/length,zero/length]

    # Write your code here
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    Pluss,Minuss,zeros=plusMinus(arr)
    print(Pluss)
    print(Minuss)
    print(zeros)