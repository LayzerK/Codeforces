import sys
input = sys.stdin.readline
from collections import deque
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  rLen,cLen = multiple_ints()
  grid = []
  for x in range(rLen):
    row = input().strip()
    grid.append([])
    for char in row:
      grid[-1].append(char)
  
  directions = [(0,1), (0,-1), (1, 0), (-1, 0), (1,1), (1,-1), (-1,1), (-1,-1)]
  ans = 0
  def bfs(row, col):
    if grid[row][col] == ".":
      return 0
    grid[row][col] = "."
    q = deque()
    q.append((row, col))
    while q:
      row, col = q.popleft()
      for dr, dc in directions:
        NR = row + dr
        NC = col + dc
        if 0 <= NR < rLen and 0 <= NC < cLen and grid[NR][NC] == "#":
          q.append((NR, NC))
          grid[NR][NC] = "."
    return 1
    
  for row in range(rLen):
    for col in range(cLen):
      ans += bfs(row, col)
  
  print(ans)
  

solve()