import sys
input = sys.stdin.readline

#if a node is before its parent than it is 1 + parent discovery. Otherwise, it is = to parent discovery.
def solve():
    n = int(input())
    adj = [[] for vertex in range(n+1)]
    order = {}
    for i in range(n-1):
        a,b = map(int, input().strip().split())
        adj[a].append(b)
        adj[b].append(a)

        order[(a,b)] = i
        order[(b,a)] = i

    discovery = [-1] * (n+1)
    discovery[1] = 1

    stack = [(1, -1)]
    while stack:
      curr, par = stack.pop()
      currorder = order[(curr, par)] if par != -1 else -1
      for child in adj[curr]:
          if child == par:
              continue
          childorder = order[(curr, child)]
          #print(currorder, childorder, curr, par, child, discovery[par])
          if childorder < currorder:
              discovery[child] = discovery[curr] + 1
          else:
              discovery[child] = discovery[curr]
          
          stack.append((child, curr))
    #print(discovery)
    print(max(discovery))
          
        



  
  
    
for tc in range(int(input())):
    solve()
