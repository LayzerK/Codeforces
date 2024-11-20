import sys
input = sys.stdin.readline
from collections import deque
from math import inf
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  
  vals = {}
  width, length, cd = multiple_ints()

  for row in range(length):
    deltas = list(input().strip().split())
    for col in range(len(deltas)):
      #print(deltas[col])
      dx, dy = map(int, deltas[col].split(","))

      vals[(col+1, row+1)] = (dx, dy)
  
  q = deque()
  visited = set()
  for x in range(1, width+1):
    q.append((0, x, 0, 0, 0, 1, True))
    visited.add((0,x,0,0,0,1, True))
  while q:
    steps, x, y, rem, dx, dy, active = q.popleft()
    #print(x,y)
    if y > length:
      print(steps)
      return
    square_x, square_y = (0,0) if (x,y) not in vals else vals[(x,y)]


    if rem == 0:
      ndx = dx if active else dx + square_x
      ndy = dy if active else dy + square_y
      ny = y + ndy
      nx = x + ndx
      NA = active ^ True
      if (nx, ny, ndx, ndy, cd-1, NA) not in visited and 0 < nx <= width and y > 0:

        q.append((steps+1, nx, ny, cd-1, ndx, ndy, NA))
        visited.add((nx, ny, ndx, ndy,cd-1, NA))
    
    if active:
      ndx = dx + square_x
      ndy = dy + square_y

      nx = x + ndx
      ny = y + ndy
      nrem = max(0, rem-1)
      if (nx, ny, ndx, ndy, nrem, active) in visited or nx < 0 or nx > width or y < 0:
        continue

      q.append((steps+1, nx, ny, nrem, ndx, ndy, active))
      visited.add((nx, ny, ndx, ndy, nrem, active))
    else:
      nx = dx + x
      ny = y + dy
      nrem = max(0, rem-1)
      if (nx, ny, dx, dy, nrem, active) in visited or nx < 0 or nx > width or y < 0:
        continue

      q.append((steps+1, nx, ny, nrem, dx, dy, active))
      visited.add((nx, ny, dx, dy, nrem, active))
  
  


solve()