import sys
from collections import defaultdict
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())

  times = []

  for i in range(n):
    a,b = multiple_ints()
    times.append((a,b))

  MX = 10**10
  
  dp = defaultdict(lambda: MX)

  #let dp[i][j] = best time we can get on person 2 assuming person 1 has used J time up until I

  dp[0] = times[0][1]
  dp[times[0][0]] = 0

  for i in range(1, n):
    ndp = defaultdict(lambda: MX)
    a,b = times[i]
    for prior_A_time, best_b_conditioned_on_A in dp.items():
      #take nums[i] for A or don't
      
      #take
      ndp[prior_A_time+a] = min(ndp[prior_A_time+a], best_b_conditioned_on_A)

      #give to B
      ndp[prior_A_time] = min(ndp[prior_A_time], best_b_conditioned_on_A + b)
    dp = ndp
  

  
  ans = MX

  for a_time, best_b_conditioned_on_A in dp.items():
    ans = min(ans, max(a_time, best_b_conditioned_on_A))
  print(ans)


solve()
    