import sys
input = sys.stdin.readline


def solve():
   n = int(input())
   par = [0, 0] + list(map(int, input().strip().split()))
   bounds = [[] for vertices in range(n+1)]

  
   for vertice in range(1, n+1):
     l,r = map(int, input().strip().split())
     bounds[vertice] = (l,r)

   #let dp[i] be the largest value for a subtree rooted at i

   dp = [0 for i in range(n+1)]
   ans = 0
   #print(par)
   for root in range(n, 0, -1):
      lbound,rbound = bounds[root]

      if dp[root] < lbound:
         dp[root] = rbound
         ans += 1
      
      #print(root, par[root])
      dp[par[root]] += min(dp[root], rbound)
   print(ans)

  
  
    
for tc in range(int(input())):
    solve()
