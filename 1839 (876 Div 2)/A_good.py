import sys
input = sys.stdin.readline
from math import ceil


def solve():
    req = 0
    n,k = map(int, input().split())

    print(ceil((n-1)/k) + 1)

for tc in range(int(input())):
    solve()


# 0 0 0 0 0 0 0 
# 1 0 0 0 0 0 1
# 1 0 0 0 0 0 1
# 1 0 0 0 0 0 1
# i =4
# 1 0 0 1 0 0 1



