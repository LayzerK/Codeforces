import sys
import itertools
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  dp = [31] * 31
  dp[0] = 0
  values = [1,3,6,10,15]
  
  for i in range(31):
    for coin in values:
      if i - coin >= 0:
        dp[i] = min(dp[i], 1 + dp[i-coin])
  
  fifteens = n//15
  
  if n <= 30:
    print(dp[n])
  else:
    all_fifteeens = n//15 + dp[n%15]
    all_but_one = n//15 - 1 + dp[n%15 + 15]
    print(min(all_fifteeens, all_but_one))

for tc in range(int(input())):
  solve()
    