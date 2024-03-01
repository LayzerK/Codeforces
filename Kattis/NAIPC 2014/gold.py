import sys
input = sys.stdin.readline
from collections import deque
import heapq
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n,m = multiple_ints()
  values = [0,0] + list(multiple_ints())
  adj = [[] for node in range(n)]
  for edge in range(m):
    a,b = multiple_ints()
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
  total = sum(values)
  #bfs to find all unweighted shortest paths

  
  q = deque()
  q.append((0,0, 1))
  mx = -1
  paths = set()
  while not paths:
    for x in range(len(q)):
      curr, profit, path = q.popleft()
      if curr == 1:
        mx = max(mx, profit)
        paths.add((path, profit))
      for nei in adj[curr]:
        
        if path & 1<<(nei):
          continue
        q.append((nei, profit+values[nei], path | 1<<(nei)))

  ans = 0
    
  def dijkstra(banned, start):
    heap = [(-start, 1)]
    profit = [-1] * n
    profit[1] = start
    while heap:
      money, curr = heapq.heappop(heap)
      
      if curr == 0:
        return -money
      for nei in adj[curr]:
        if banned & (1<<nei) and -(money+values[nei]) > profit[nei]:
          heapq.heappush(heap, (money+values[nei], nei))
          profit[nei] = -(money+values[nei])
        elif -money > profit[nei] and not banned & (1<<nei):
          heapq.heappush(heap, (money, nei))

  for banned, money in paths:
    if money == mx:
      print(dijkstra(banned, money))
      return
  print(ans)

          
      
  

solve()
    