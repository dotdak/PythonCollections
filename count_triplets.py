import math
from collections import Counter
def count_triplets(arr, r):
    ans = 0
    count_map = {}
    if r == 1:
        for i in Counter(arr).values():
            ans += i**3
    for num in arr:
        order_1 = num//r
        if order_1:
            count_map.setdefault(order_1, [0, 0])
            count_map[order_1][1] += count_map[order_1][0]
        order_2 = num//r//r
        if order_2:
            count_map.setdefault(order_2, [0, 0])
            ans += count_map[order_2][1]
        count_map.setdefault(num, [0, 0])
        count_map[num][0] += 1
    return ans
if __name__ == '__main__':
    f = open('/d/count_triplets_testcases.txt', 'r')
    n_cases = int(f.readline().rstrip())
    for _ in range(n_cases):
        nr = f.readline().rstrip().split()
        n = int(nr[0])
        r = int(nr[1])
        arr = list(map(int, f.readline().rstrip().split()))
        ans = count_triplets(arr, r)
        true_ans = int(f.readline().rstrip())
        print('ans= {} - true_ans= {}'.format(ans, true_ans))
    f.close()

