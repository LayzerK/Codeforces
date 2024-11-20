import sys
from bisect import bisect_left
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  days = list(multiple_ints())
  n = len(days)

  one,seven, thirty = multiple_ints()

  
  dp = {}
  def dfs(day):
    if day > days[-1]:
      return 0
    if day in dp:
      return dp[day]
    i = bisect_left(days, day)

    d = days[i]

    day = max(day, d)

    ans = min(dfs(day+1) +  one, dfs(day+7) + seven, dfs(day+30) + thirty)
    dp[day] = ans
    return ans
  
  ans = dfs(1)
  print(ans)
  


solve()
    