#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    sum_max = arr[0]
    sum_subarr = arr[0]
    blocks = []
    tracker = arr[0] if arr[0] > 0 else 0
    for i in range(1, len(arr)):
        sum_max = max(sum_max, sum_max + arr[i], arr[i])
        if arr[i] > 0:
            # sum_subarr = max(sum_subarr, arr[i], sum_subarr + arr[i])
            tracker += arr[i]
        elif arr[i] < 0 and i != len(arr) - 1:
            if tracker >= 0:
                blocks.append(tracker)
            else:
                sum_subarr = max(sum_subarr, sum(blocks))
                blocks = []
            tracker = arr[i]
    if sum_max < 0:
        sum_subarr = sum_max
    return [sum_subarr, sum_max]

if __name__ == '__main__':
    f = open('/d/max_subarray_testcases.txt', 'r')
    t = int(f.readline())

    for t_itr in range(t):
        n = int(f.readline())
        arr = list(map(int, f.readline().rstrip().split()))
        result = maxSubarray(arr)
        print(result)
    print('true ans =')
    for _ in range(t):
        print(f.readline().rstrip())


