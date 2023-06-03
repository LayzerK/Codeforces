import sys
input = sys.stdin.readline
from collections import defaultdict
def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    #number of inversions = counting req

    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            print("YES")
            return
    print("NO")
    


for tc in range(int(input())):
    solve()