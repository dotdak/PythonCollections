#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n = len(arr)
    new_arr = [0]*n
    new_arr[0:2] = arr[0:2]
    new_arr[2] = max(arr[2] + arr[0], arr[2], arr[0])
    ans = -20000000
    for i in range(3, n):
        if arr[i] > 0:
            new_arr[i] = max(arr[i], arr[i] + new_arr[i-2], arr[i] + new_arr[i-3])
        else:
            new_arr[i] = max(new_arr[i-2], new_arr[i-3])
        ans = max(ans, new_arr[i])
    return ans
if __name__ == '__main__':
    f = open('/d/max_array_sum_testcases.txt', 'r')
    n = int(f.readline().rstrip())
    arr = list(map(int, f.readline().rstrip().split()))
    res = maxSubsetSum(arr)
    print(res, ', true_ans =', f.readline())
    f.close()

