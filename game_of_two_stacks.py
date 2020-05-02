from collections import deque

def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    count = 0
    ssum = 0
    stack_a = deque(a)
    stack_b = deque(b)
    i = j = 0
    '''
    while ssum <= x:
        if stack_a and stack_a[0] < stack_b[0]:
            ssum += stack_a.popleft()
            count += 1
        else:
            ssum += stack_b.popleft()
            count += 1
    return count - 1
    '''
    while ssum <= x and i < len(a):
        i += 1
        ssum += a[i]
    count = i - 1
    while i >= 0 and j < len(b):
        ssum += b[j]
        j += 1
        while ssum > x and i > 0:
            ssum -= a[i]
            i -= 1
        if i + j > count:
            count = i + j
    return count

if __name__ == '__main__':
    f = open('/d/testcases.txt', 'r')
    g = int(f.readline().rstrip())

    for g_itr in range(g):
        nmx = f.readline().rstrip().split()
        n = int(nmx[0])
        m = int(nmx[1])
        x = int(nmx[2])
        a = list(map(int, f.readline().rstrip().split()))
        b = list(map(int, f.readline().rstrip().split()))
        result = twoStacks(x, a, b)
        print(result)
    f.close()

