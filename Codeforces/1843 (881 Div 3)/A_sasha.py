import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))

    arr.sort()

    left = 0
    right = n-1
    ans = 0
    while left <= right:
        ans += arr[right] - arr[left]
        left += 1
        right -= 1
    print(ans)

for tc in range(int(input())):
    solve()