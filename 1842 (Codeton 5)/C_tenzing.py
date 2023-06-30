import sys
input = sys.stdin.readline
from math import inf
def solve():
    n = int(input())
    arr = [0] + list(map(int, input().strip().split()))

    dp = [0] * (n+1)

    before = [float(inf)] * (n+1)

    #let before equal the minimal number of elements to the left of a given number

    for i in range(1, n+1):
        num = arr[i]

        dp[i]= min(1 + dp[i-1], before[num])

        before[num] = min(dp[i-1], before[num])
    
    print(n - dp[-1])

for tc in range(int(input())):
    solve()