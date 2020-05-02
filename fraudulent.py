#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def rebuild_count_map(count_map, old_val, new_val):
    count_map[old_val] -= 1
    count_map[new_val] += 1

def median(count_map, d):
    half = 0
    j = 0
    for i in range(len(count_map)):
        if count_map[i] > 0:
            half += count_map[i]
            if half*2 > d:
                break
            j = i
    return i if d%2 or count_map[i] > 1 and (half - count_map[i])*2 != d else (i + j)/2

def activityNotifications(expenditure, d):
    ans = 0
    MAX = 300
    count_map = [0]*MAX
    for i in expenditure[:d]:
        count_map[i] += 1
    for i in range(d, len(expenditure)):
        med = median(count_map, d)
        rebuild_count_map(count_map, expenditure[i-d], expenditure[i])
        if expenditure[i] >= med*2:
            ans += 1
    return ans

if __name__ == '__main__':
    f = open('/d/fraudulent_testcases.txt', 'r')
    nd = f.readline().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, f.readline().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(result)
    true_ans = f.readline().rstrip()
    print('true ans =', true_ans)
