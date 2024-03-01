import sys
input = sys.stdin.readline
from math import ceil

def solve():
    n = int(input())
    # print(n//3)
    f = ceil(n/3) + 1
    s = ceil(n/3) if (n-f-ceil(n/3) != 0) else ceil(n/3) - 1
    t = n - f - s
    print(s,f,t)
for tc in range(int(input())):
    solve()