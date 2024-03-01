import sys
input = sys.stdin.readline
import collections
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  q = collections.deque()
  ans = 0

  rLen,cLen = multiple_ints()
  
  grid = []
  
  for row in range(rLen):
    r = input().strip()
    grid.append([])
    for c in r:
      grid[-1].append(int(c))
  #print(grid)
  q = collections.deque()
  visited = set()

  for row in range(rLen):
    if grid[row][0] == 0:
      q.append((row, 0))
      visited.add((row, 0))
    else:
      #print(row, 0)
      ans += 1
    if grid[row][-1] == 0 and (row, cLen -1) not in visited:
      q.append((row, cLen-1))
      visited.add((row, cLen-1))

    elif grid[row][cLen-1] == 1:
      #print(row, cLen-1)
      ans += 1
      


  for col in range(cLen):
    if grid[0][col] == 0 and (0, col) not in visited:
      q.append((0, col))
      visited.add((0, col))
    elif grid[0][col] == 1:
      #print(0, col)
      ans += 1
    if grid[rLen-1][col] == 0 and rLen != 1 and (rLen-1, col) not in visited:
      q.append((rLen-1, col))
      visited.add((rLen-1, col))
    elif grid[rLen-1][col] == 1:
      ans += 1  

  #print(ans)
  directions = [(0,1), (0,-1), (1,0), (-1,0)]

  while q:
    row, col = q.popleft()
    
    for dr, dc in directions:
      NR = row + dr
      NC = col + dc
      
      if 0 <= NR < rLen and 0 <= NC < cLen and (NR, NC) not in visited:
        
        if grid[NR][NC] == 0:
          q.append((NR, NC))
          visited.add((NR, NC))
        else:
          #print(NR, NC, row, col)
          ans += 1
  print(ans)
      

  

solve()
    