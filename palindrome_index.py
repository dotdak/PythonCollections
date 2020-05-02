#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def check_palindrome(s):
    middle = len(s) // 2
    for i in range(middle + 1):
        j = len(s) - i - 1
        if s[i] != s[j]:
            return False
    return True

def palindromeIndex(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            if check_palindrome(s[:i] + s[i+1:]):
                return i
            elif check_palindrome(s[:j] + s[j+1:]):
                return j
            else:
                return -1
        i += 1
        j -= 1
    return -1

if __name__ == '__main__':
    f = open('/d/palindrome_index_testcases.txt', 'r')
    q = int(f.readline())

    for q_itr in range(q):
        s = f.readline().rstrip()

        result = palindromeIndex(s)
        print(result)
    print('true ans = ')
    for _ in range(q):
        print(f.readline().rstrip())

    f.close()

