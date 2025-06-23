import sys
input = sys.stdin.readline
from functools import lru_cache
sys.setrecursionlimit(1000000)

def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  rows, cols, mx = multiple_ints()

  avg = mx / 2
  
  @lru_cache(maxsize=None)
  def dfs(row, col):

    if row == 1 and col == 1:
      return 0
    elif row > col:
      return dfs(col, row)
    elif row == 1:
      return avg/2 + dfs(row, col-1)
    else:
      #we are on some interior point

      down = dfs(row-1, col)
      right = dfs(row, col-1)

    

      expensive = max(down, right)
      cheap = min(down, right)
      diff = expensive - cheap
      #in expectation there is a 50% chance it is pointing to the cheap side and we take that
      #otherwise, it is pointing to the expensive side
      #if we wait time X, we 'gain' diff, but lose our wait time


      #since we are operating on a continous timescale, we only wait if our time is less than diff, since this is uniformly distributed from 0...M,
      #the average wait time of something less than diff is just diff/2

      #the probability that this occurs is diff/mx

      #this gives (delta^2)/2*mx
      #in all other cases we wait. This wait distribution mx-diff/mx


      expensive_cost = ((cheap + (diff/2)) * (diff/mx)) + expensive * ((mx-diff)/mx)

      ans =  (cheap + expensive_cost)/2
      #dp[(row, col)] = ans
      return ans
  print(dfs(rows, cols))


solve()
    