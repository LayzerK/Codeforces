import sys
from math import inf
import heapq
from collections import defaultdict
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve(n, edges, queries, start):  
  
  adj = defaultdict(list)
  
  for edge in range(edges):
    u,v,cost = multiple_ints()
    adj[u].append((v, cost))
  def dijk():
    heap = [(0, start)]
    costs = defaultdict(lambda: inf)
    costs[start] = 0
    while heap:
      cost, curr = heapq.heappop(heap)
      
      if cost > costs[curr]:
        continue
      
      for nei, edge_cost in adj[curr]:
        nei_cost = edge_cost + cost
        
        if nei_cost < costs[nei]:
          heapq.heappush(heap, (nei_cost, nei))
          costs[nei] = nei_cost
    return costs
  
  ans = dijk()
  for q in range(queries):
    end = int(input())
    if end in ans:
      print(ans[end])
    else:
      print("Impossible")
    
n,edges,queries, start = multiple_ints()

while n != 0:
  solve(n, edges, queries, start)
  n,edges,queries,start = multiple_ints()



    