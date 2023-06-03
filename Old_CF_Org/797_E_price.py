import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n,k = map(int, input().strip().split())

    arr = list(map(int, input().strip().split()))


    ans = 0
    
    for i, num in enumerate(arr):
        ans += num//k
        arr[i] = num%k
    
    arr.sort()


    left = 0
    right = len(arr) - 1

    while left < right:
        
        while left < right and arr[left] + arr[right] < k:
            left += 1
        
        if left != right:
            ans += 1
            left += 1
            right -= 1
    print(ans)
    
for tc in range(int(input())):
    solve()
