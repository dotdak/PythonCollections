#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort function below.
def insertionSort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1
        arr[j + 1] = key
    return count

if __name__ == '__main__':
    f = open('/d/insertion_sort_testcases.txt', 'r')
    t = int(f.readline())
    for t_itr in range(t):
        n = int(f.readline())
        arr = list(map(int, f.readline().rstrip().split()))
        result = insertionSort(arr)
        print(result)
    f.close()



