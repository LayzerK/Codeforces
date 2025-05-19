import sys
input = sys.stdin.readline
from collections import defaultdict
from math import gcd
def solve():
    n = int(input())

    arr = list(map(int, input().strip().split()))

    skip = defaultdict(int)
    arr.sort()
    ans = [arr[-1]]
    arr.pop()
    
    while len(ans) < n and arr:
        while arr and skip[arr[-1]]:
            skip[arr[-1]] -= 1
            arr.pop()

        if arr:
            for element in ans:
              #print(arr, ans, element)
              x = gcd(element, arr[-1])
              skip[x] += 2
            ans.append(arr[-1])
            arr.pop()
    #print(skip)
    print(*ans)
        



solve()