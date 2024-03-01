import sys
from math import inf
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve(depots, attacks):
    arr = list(multiple_ints())

    #dp[i][j][m] = most you can get from 1 to J with M remaining
    
    prefix = [arr[0]]

    for i in range(1, len(arr)):
        prefix.append(arr[i] * prefix[-1])
    
    memo = {}

    def dfs(lb, rb, rem):
      if (lb, rb, rem) in memo:
          return memo[(lb,rb,rem)]
      if rem == 0:
          left_pre = prefix[lb] if lb != 0 else 1
          val = prefix[rb]//left_pre
          return val
      if lb == rb:
          return arr[lb]
      cost = inf

      for cut in range(lb, rb):
          avail = rem - 1

          for left_strikes in range(0, rem):
              left_side = dfs(lb, cut, left_strikes)
              right_side = dfs(cut+1, rb, avail-left_strikes)
              cost = min(cost, left_side+right_side)
      memo[(lb,rb,rem)] = cost
      return cost
    
    print(dfs(0, depots-1, attacks), "ans")
    print(prefix)

    

while True:
    N, M = multiple_ints()

    if N == M == 0:
        break
    solve(N,M)
    