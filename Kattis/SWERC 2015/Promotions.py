import sys
input = sys.stdin.readline
import collections
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  start, end, n, edges = multiple_ints()
  adj = [[] for emp in range(n)]
  
  indegree = [0 for emp in range(n)]
  
  for edge in range(edges):
    x,y = multiple_ints()
    indegree[y] += 1
    adj[x].append(y)
  
  q = collections.deque()
  
  for i, cnt in enumerate(indegree):
    if cnt == 0:
      q.append(i)
  levels = []
  while q:
    c_level = []
    for x in range(len(q)):
      curr = q.popleft()
      c_level.append(curr)
      for nei in adj[curr]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
          q.append(nei)
    levels.append(c_level)
  avail = 0
  LEQA = 0
  LEQB = 0
  GEB = 0
  prior = 0
  #print(levels)
  for level in levels:

    avail += len(level)
    if avail <= start:
      LEQA = avail
    if avail <= end:
      LEQB = avail
    
    if avail > end and GEB == 0 and prior >= end:
      GEB = n - prior
    prior = avail
  

  print(LEQA)
  print(LEQB)
  print(GEB)

          
solve()
    