import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  adj = [[] for node in range(n+1)]
  colors = [-1 for node in range(n+1)]

  ans = [0] * (n-1)
  for node in range(1, n+1):
    colors[node] = int(input())

  for edge in range(n-1):
    a,b = multiple_ints()
    adj[a].append((b,edge))
    adj[b].append((a, edge))
  

  def dfs(curr, par):
      
    
 

solve()