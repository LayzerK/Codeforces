import sys
input = sys.stdin.readline
from functools import cache
def solve(bound):
      bound = str(bound)    
      k = len(bound)
      #classic pattern of subtract
      def dfs(i, cnt, upper):
          #print(i, bound)
          if i > k or cnt > 3:
              return 0
          if i == k:
              return 1
          if dp[i][upper][cnt] != -1:
              return dp[i][upper][cnt]
          rb = 9 if not upper else int(bound[i])
          ans = 0
          for digit in range(rb+1):
              #print(i, rb, upper, digit)
              if digit != 0:
                  
                ans += dfs(i+1, cnt+1, upper and digit == int(bound[i]))
              else:
                ans += dfs(i+1, cnt, upper and digit == int(bound[i]))
          dp[i][upper][cnt] = ans
          return ans
              
      big = dfs(0, 0, True)
      return big        
        

for tc in range(int(input())):
    l,r = map(int, input().strip().split())
    dp=[[[-1 for i in range(4)]for bnd in range(2)]for cnt in range(24)]
    big = solve(r)
    dp=[[[-1 for i in range(4)]for bnd in range(2)]for cnt in range(24)]
    small = solve(l-1)

    print(big-small)