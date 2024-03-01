import sys
input = sys.stdin.readline
from collections import defaultdict
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  visited = set()
  freqs = defaultdict(lambda: defaultdict(list))
  adj = defaultdict(list)
  
  def dfs(curr, par):
    stack = [(curr, par)]
    if curr in visited:
      return
    visited.add(curr)
    while stack:
      curr, par = stack.pop()
      for nei in adj[curr]:
        if nei == par or nei in visited:
          continue
        stack.append((nei, curr))
        visited.add(nei)

  for edge in range(n-1):
    a,b,color = multiple_ints()
    adj[a].append(b)
    adj[b].append(a)
    freqs[a][color].append(b)
    freqs[b][color].append(a)

  for node in range(1, n+1):
    for color, children in freqs[node].items():
      if len(children) >= 2:
        for child in children:
          if child in visited:
            print(0)
            return
          dfs(child, node)
  print(n-len(visited))
  for node in range(1, n+1):
    if node not in visited:
      print(node)
    
    
solve()
    