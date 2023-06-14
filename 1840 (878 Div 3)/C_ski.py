import sys
input = sys.stdin.readline

def solve():
    n,k,q = map(int, input().strip().split())

    arr = list(map(int, input().strip().split()))

    ans = 0

    left = 0
    
    for right, temp in enumerate(arr):
        if temp > q:
            
            left = right + 1
            continue
        sz = right - left + 1
        if sz >= k:
            ans += sz-k+1
    print(ans)
        

for tc in range(int(input())):
    solve()