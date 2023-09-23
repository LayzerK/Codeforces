import sys
input = sys.stdin.readline
from itertools import accumulate
import bisect

def check(height, arr, prefix, x):
    
    i = bisect.bisect_right(arr, height-1)

    uncovered = prefix[i-1] if i > 0 else 0

        

    return (i*height - uncovered) <= x
        
    
def solve():
    
    n,x = map(int, input().strip().split())
    #print(n,x, "Mo")
    arr = sorted(list(map(int, input().strip().split())))
    prefix = list(accumulate(arr))

    left = 0
    right = 10**20

    while left <= right:
        mid = (left+right)//2

        if check(mid, arr, prefix, x):
            left = mid + 1
        else:
            right = mid - 1
    #print(check(2, arr, x))
    print(right)
            
    

for tc in range(int(input())):
    solve()