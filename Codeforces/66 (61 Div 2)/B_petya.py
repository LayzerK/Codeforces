import sys
input = sys.stdin.readline


#find the maximum subarray such that the left and right sides of the middle
#are monotonically non increasing
def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = 0
    for mid in range(n):
        left = mid
        right = mid
        while left > 0 and arr[left - 1] <= arr[left]:
            left -= 1
        while right < n - 1 and arr[right + 1] <= arr[right]:
            right += 1
        ans = max(ans, right-left+1)
        #print(left, right, ans)

    print(ans)
    
    


solve()