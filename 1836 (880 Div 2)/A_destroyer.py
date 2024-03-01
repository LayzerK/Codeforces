import sys
input = sys.stdin.readline
from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    
    cnts = Counter(arr)

    for x in range(1, 100):
        if cnts[x] > cnts[x-1]:
            print("NO")
            return
    print("YES")

for tc in range(int(input())):
    solve()