#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    ls = []
    current_char = None
    count = 0
    result = 0
    for char in s:
        if char == current_char:
            count += 1
        else:
            if current_char is not None:
                ls.append((current_char, count))
            count = 1
            current_char = char
    ls.append((current_char, count))
    for i in ls:
        result += (i[1]*(i[1] + 1)) // 2

    for i in range(1, len(ls) - 1):
        if ls[i - 1][0] == ls[i + 1][0] and ls[i][1] == 1:
            num = ls[i - 1][1] if ls[i - 1][1] < ls[i + 1][1] else ls[i + 1][1]
            result += num
    return result

if __name__ == '__main__':
    f = open('/d/palindrome_testcases.txt', 'r')
    n = int(f.readline())
    s = f.readline()
    result = substrCount(n, s)

    print(result)
