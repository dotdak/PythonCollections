#!/bin/python3

import os
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    start = 0
    m = len(s1)
    n = len(s2)
    C = [[0 for col in range(m + 1)] for row in range(n + 1)]
    while start <= m and start <= n and s1[start] == s2[start]:
        start += 1
    while start <= m and start <= n and s1[m - 1] == s2[n - 1]:
        m -= 1
        n -= 1
    for i in range(start + 1, m + 1):
        for j in range(start + 1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
        print(C[i])
    return C[m][n] + start

if __name__ == '__main__':
    f = open('/d/longest_common_subsequences.txt', 'r')
    s1 = f.readline().rstrip()
    s2 = f.readline().rstrip()
    result = commonChild(s1, s2)
    print(result)
