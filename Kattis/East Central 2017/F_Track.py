import sys
input = sys.stdin.readline
from collections import defaultdict
from math import comb
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input()) + 1
  sys.setrecursionlimit(n+100)

  adj = [[] for node in range(n)]
  
  for edge in range(n-1):
    a,b = multiple_ints()
    adj[a].append(b)
    adj[b].append(a)
  
  subtree = [0] * n
  
  def subtreesize(curr, par):
    children = 0
    for child in adj[curr]:
      if child == par:
        continue
      children += subtreesize(child, curr)
      
    subtree[curr] = children + 1
    return children + 1

  def dfs(curr, par):
    above = n - subtree[curr]
    
    groups = [above] + [subtree[child] for child in adj[curr] if child != par]
    
    if len(groups) == 1:
      return (0,0)
    groups.sort(reverse = True)
    disconnect = comb(n-1, 2)
    for x in groups:
      disconnect -= comb(x, 2)
    
    added_back = groups[0] * groups[1]
    rem = disconnect - added_back
    

    #if we delete this node, then we disconn  
    
    
    for child in adj[curr]:
      if child == par:
        continue
      child_dis, child_rem = dfs(child, curr)
      
      if child_dis > disconnect:
        disconnect = child_dis
        rem = child_rem
    #print(disconnect, rem)
    return (disconnect, rem)
  subtreesize(0, -1)
  disconnected, added_back = dfs(0, -1)
 
  print(disconnected, added_back)
    


solve()