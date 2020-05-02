#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseShuffleMerge function below.
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

def reverseShuffleMerge(s):
    n = len(s)//2
    ans = '}'
    for i in range(n + 1):
        sub_str = s[i:i+n]
        remaining_str = s.replace(sub_str, '')
        if sorted(sub_str) == sorted(remaining_str):
            sub_reversed = reverse(sub_str)
            ans = min(ans, sub_reversed)
    return ans

if __name__ == '__main__':
    f = open('/d/merge_reverse_shuffle_testcases.txt', 'r')
    s = f.readline().rstrip()
    result = reverseShuffleMerge(s)
    ans = f.readline().rstrip()
    print(result)
    print(ans)
    print(result == ans)
    f.close()
