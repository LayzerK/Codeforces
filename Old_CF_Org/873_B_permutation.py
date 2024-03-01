from math import gcd
import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    locs = {}

    for i, num in enumerate(arr):
        locs[num] = i+1
    ans = 0
    for num in range(1, n+1):
        if locs[num] != num:
            #print(abs(num-locs[num]), num)
            dist = abs(num-locs[num])
            ans = gcd(ans, dist) if ans else dist
    print(ans)


for tc in range(int(input())):
    solve()
