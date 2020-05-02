#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    a_ls = list(a)
    b_ls = list(b)
    while a_ls and b_ls:
        if a_ls[0].isupper():
            if a_ls[0] == b_ls[0]:
                a_ls.pop(0)
                b_ls.pop(0)
            else:
                #print(''.join(a_ls[0:]))
                return 'NO'
        elif a_ls[1].capitalize() == b[0]:
            a_ls.pop(0)
        else:
            a_ls.pop(0)
    while a_ls:
        if a_ls.pop(0).isupper():
            return 'NO'
    return 'NO' if b_ls else 'YES'

if __name__ == '__main__':
    f = open('/d/abbreviation_testcases.txt', 'r')
    q = int(f.readline().rstrip())

    for q_itr in range(q):
        a = f.readline().rstrip()
        b = f.readline().rstrip()
        result = abbreviation(a, b)
        print(result)
    for _ in range(q):
        ans = f.readline().rstrip()
        print('true ans =', ans)
    f.close()
    
