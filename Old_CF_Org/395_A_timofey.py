import sys
input = sys.stdin.readline


def solve():
  n = int(input())
  adj = [[] for x in range(n+1)]

  for edge in range(n-1):
    a,b = map(int, input().strip().split())

    adj[a].append(b)
    adj[b].append(a)

  colors = list(map(int, input().strip().split()))
  cnts = [0] * (n+1)
  stack = [(1, -1)]

  while stack:
    curr, par = stack.pop()
    for nei in adj[curr]:
     
      cnts[curr] += int(colors[curr-1] != colors[nei-1])

      if nei == par:
        continue
      stack.append((nei, curr))
    

  root = 1
  diff = 0

  for i in range(1, n+1):
    if cnts[i] > diff:
      root = i
      diff = cnts[i]
  
  if diff == 0:
    print("YES")
    print(1)
    return


  def check(start, par):
    c = colors[start-1]

    stack = [(start, par)]

    while stack:
      curr, par = stack.pop()
      #print(curr, "here")
      for nei in adj[curr]:
        if nei == par:
          continue

        if colors[nei-1] != c:
          return False
        stack.append((nei, curr))
    return True
  #print(diff, cnts)
  for child in adj[root]:
    #print(child, "checking ch ild")
    if not check(child, root):
      print("NO")
      return
  print("YES")
  print(root)
    
solve()