import sys
input = sys.stdin.readline
from math import ceil
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    a,b, capacity = multiple_ints()

    diff = abs(a-b)/2

    print(ceil(diff/capacity))

for tc in range(int(input())):
    solve()
    