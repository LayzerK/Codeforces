import heapq
from collections import defaultdict
testcases = int(input())
for testcase in range(testcases):
    needed = 0
    freqs = defaultdict(int)

    n = int(input())

    dolls = sorted(map(int, input().split()))

    for size in dolls:
        if freqs[size-1] < 1:
            needed += 1
        else:
            freqs[size-1] -= 1
        freqs[size] += 1
    print(needed)
