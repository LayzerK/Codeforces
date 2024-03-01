import sys
import heapq
from collections import defaultdict
from math import inf
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  adj = defaultdict(lambda: defaultdict(lambda: inf))
  n,m = multiple_ints()
  rank = [1 for x in range(n+1)]
  par = [x for x in range(n+1)]
  edges = [tuple(multiple_ints()) for edge in range(m)]
  
  def find(node):
      if par[node] != node:
          par[node] = find(par[node])
      return par[node]
  
  def union(n1, n2):
      p1 = find(n1)
      p2 = find(n2)
      
      if rank[p1] > rank[p2]:
          par[p2] = p1
      elif rank[p2] > rank[p1]:
          par[p1] = p2
      
      else:
          par[p2] = p1
          rank[p1] += 1
  for a,b,cost in edges:
     if cost == 0:
        union(a,b)
  #print(edges)
  for a,b,cost in edges:
     p1 = find(a)
     p2 = find(b)
     if p1 == p2:
        continue
     adj[p1][p2] = min(adj[p1][p2], cost)
     adj[p2][p1] = adj[p1][p2]
  cities = list(multiple_ints())
  indices = defaultdict(list)
  starting_mask = 0

  for i, city in enumerate(cities):
    if find(city) == find(1):
      starting_mask |= 1 << i
    indices[find(city)].append(i)
  full = (1<<7) - 1
  costs = defaultdict(lambda: inf)
  costs[(find(1), starting_mask)] = 0
  heap = [(0,find(1),starting_mask)]
  while heap:
    cost, curr, mask = heapq.heappop(heap)
    #print(cost, curr, mask, "here")
    if cost > costs[(curr, mask)]:
      continue
    if mask == full:
      print(cost)
      return
    
    for nei, edge_cost in adj[curr].items():
      new_cost = edge_cost + cost
      new_mask = mask
      for indice in indices[nei]:
        new_mask |= 1<< indice
      if new_cost < costs[(nei, new_mask)]:
        costs[(nei, new_mask)] = new_cost
        heapq.heappush(heap, (new_cost, nei, new_mask))
  
  


solve()
    