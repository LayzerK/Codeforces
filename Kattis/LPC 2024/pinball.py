import sys
input = sys.stdin.readline
from bisect import bisect_left
from collections import defaultdict
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  flippers = defaultdict(list)

  n, end = multiple_ints()
  for flip in range(n):
    x,y,k = multiple_ints()
    vals = list(multiple_ints())
    flippers[x].append((y, vals))
  
  for x in flippers:
    flippers[x].sort()
  dp = {}
  def dfs(x, y):
    print(x,y)
    if (x,y) in dp:
      return dp[(x,y)]
    nxt = bisect_left(flippers[x], y, key = lambda a:a[0])
    if nxt >= len(flippers[x]):
      if x == 0:
        return 1
      else:
        return 0
    
    ny, disps = flippers[x][nxt]
    k = len(disps)

    ans = 0

    for disp in disps:
      ans += dfs(flippers[nxt][0], x + disp)/k
    dp[(x,y)] = ans
    return ans
  
  print(dfs(0,0))
    

solve()