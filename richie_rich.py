#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
'''
def highestValuePalindrome(s, n, k):
    middle = n//2
    s1 = None
    s2 = None
    if n % 2:
        s1 = s[:middle]
        s2 = s[:middle:-1]
    else:
        s1 = s[:middle]
        s2 = s[:middle-1:-1]
    diff_index = []
    for i in range(middle):
        if s1[i] != s2[i]:
            diff_index.append(i)
    print('diff_index = ', diff_index)

    if len(diff_index) <= k:
        to_9_total = k - len(diff_index)
    else:
        return '-1'
    result = ''
    for i in range(middle):
        val = None
        if i in diff_index:
            if to_9_total > 0:
                to_9_total -= 1
                val = '9'
            else:
                val = max(s[i], s[n - i - 1])
        else:
            val = s[i]
        result += val
    middle_char = s[middle] if n % 2 else ''
    return result + middle_char + result[::-1]
'''
def highestValuePalindrome(s, n, k):
    nums = list(map(int, s))
    middle = n // 2
    indexes = []
    for i in range(middle):
        if nums[i] != nums[n - 1 - i]:
            indexes.append(i)
    if k - len(indexes) < 0:
        return '-1'
    i = 0
    while i < n//2 and k - len(indexes) > 0:
        j = n - 1 - i
        if indexes and i == indexes[0]:
            indexes.pop(0)
        if nums[i] != 9 and nums[j] != 9:
            k -= 2
        elif nums[i] == 9 or nums[j] == 9:
            k -= 1
        nums[i] = 9
        nums[j] = 9
        i += 1
    for ind in indexes:
        j = n - 1 - ind
        maximum = max(nums[ind], nums[j])
        nums[ind] = nums[j] = maximum
    return ''.join(map(str, nums))

if __name__ == '__main__':
    f = open('/d/richie_rich_testcases.txt', 'r')
    nk = f.readline().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    print(n, k)
    s = f.readline().rstrip()
    result = highestValuePalindrome(s, n, k)
    ans = f.readline().rstrip()
    for i in range(len(result)):
        if result[i] != ans[i]:
            print(result[i:len(result)//2])
            print('------------------------')
            print(ans[i:len(ans)//2])
            break
    # print(result)
    f.close()

