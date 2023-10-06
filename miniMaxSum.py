import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Find the minimum and maximum values in the list
    min_val = min(arr)
    max_val = max(arr)
    
    # Calculate the sum of all elements in the list
    total_sum = sum(arr)
    
    # Calculate the sum of elements after excluding the minimum and maximum values
    min_sum = total_sum - max_val
    max_sum = total_sum - min_val
    
    return min_sum, max_sum

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    min_sum, max_sum = miniMaxSum(arr)
    print(min_sum, max_sum)
