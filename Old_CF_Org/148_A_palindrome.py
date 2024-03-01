from collections import defaultdict
from collections import Counter
import sys
input = sys.stdin.readline


def solve():
    s = input()

    cnts = Counter(s)

    bucket = defaultdict(int)

    for char, freq in cnts.items():
        bucket[freq] += 1

    if sum(bucket.values()) - bucket[1] >= 2:
        print("yes")

    else:
        print("no")


for tc in range(int(input())):
    solve()
