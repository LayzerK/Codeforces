import sys
input = sys.stdin.readline
from collections import Counter
from math import ceil

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    cnts = Counter(arr)
    total = sum(arr)

    if total >= 0:
        if cnts[-1] % 2 == 1:
            print(1)
        else:
            print(0)
    else:
        req = ceil(abs(total)/2)
        rem = cnts[-1] - req
        #print(req, rem, total)
        print(req + int(rem%2 == 1))

for tc in range(int(input())):
    solve()