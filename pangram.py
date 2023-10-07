#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower()
    
    # Inisialisasi sebuah set kosong untuk menyimpan huruf yang sudah ada
    huruf_terdapat = set()
    
    # Loop melalui setiap karakter dalam s
    for char in s:
        # Periksa apakah karakter adalah huruf alfabet dan belum ada dalam set
        if char.isalpha() and char not in huruf_terdapat:
            huruf_terdapat.add(char)
    
    # Periksa apakah set huruf_terdapat memiliki panjang 26 (jumlah huruf alfabet)
    if len(huruf_terdapat) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
