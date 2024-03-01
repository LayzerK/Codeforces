import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    

    for i in range(n-1, 0, -2):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            print("NO")
            return
    print("YES")
            

for tc in range(int(input())):
    solve()