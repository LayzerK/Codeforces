import sys
from collections import deque()
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  colors = [-1]
  cnts = [0] * (n+2)
  indegree = [0] * (n+1)
  for i in range(n):
    colors.append(int(input()))
    cnts[colors[-1]] += 1

  adj = [[] for i in range(n+1)]
  edges=  []
  emap = {}
  ans = [0] * (n-1)
  for edge in range(n-1):
    
    a,b = multiple_ints()
    emap[(a,b)] = edge
    emap[(b,a)] = edge

    edges.append((a,b))
    adj[a].append(b)
    adj[b].append(a)
    indegree[a] += 1
    indegree[b] += 1
  
  leafs = []

  for i in range(1, n+1):
    if indegree[i] == 1:
      leafs.append(i)
    
  q = deque()

    
solve()