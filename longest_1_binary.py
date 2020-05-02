def longest_run(n):
    maximum = 0
    count = 0
    while n > 0:
        if n % 2:
            count += 1
            maximum = max(count, maximum)
        else:
            count = 0
        n //= 2
    return maximum
print(longest_run(242))
