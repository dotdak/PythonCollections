#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import time

# Complete the freqQuery function below.
def freqQuery(queries):
    count = {}
    for i in queries:
        command, val = i
        if command == 1:
            count.setdefault(val, 0)
            count[val] += 1
        elif command == 2:
            count.setdefault(val, 0)
            count[val] = count[val] - 1 if count[val] > 0 else 0
        elif command == 3:
            yield 1 if val in count.values() else 0

if __name__ == '__main__':
    f = open('/d/frequencies_queries_testcases.txt', 'r')
    q = int(f.readline().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, f.readline().rstrip().split())))
    t = time.time()
    ans = freqQuery(queries)
    print('\n'.join(map(str, ans)))
    print(time.time() - t)
    f.close()
