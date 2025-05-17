import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  cLen, rLen = multiple_ints()
  directions = [(1,0), (0, 1), (-1,0), (0, -1)]
  robots, instructions = multiple_ints()

  dmap = {"N": 0, "S": 2, "E": 1, "W": 3}
  grid = [[0 for i in range(cLen+1)] for j in range(rLen+1)]
  locs = {}
  v = True
  for robot in range(1, robots+1):
    col, row, direction = input().strip().split()
    col, row = int(col), int(row)
    grid[row][col] = (dmap[direction], robot)
    locs[robot] = (row, col)
  #print(grid)
  for action in range(instructions):
    robot, atype, num = input().strip().split()
    if v == False:
      continue 
    num = int(num)
    robot = int(robot)
    r,c = locs[robot]
    face = grid[r][c][0]
    if atype == "F":
      grid[r][c] = 0
      dr, dc = directions[face]
      for i in range(num):
        r += dr
        c += dc
        #print(r, c, "HERE", dr, dc, face)
        if(r == rLen+1 or r == 0 or c == 0 or c == cLen+1):
          print(f"Robot {robot} crashes into the wall")
          v = False
          break
        if grid[r][c] != 0:
          #print(r, c, "JHERER", dr, dc)
          print(f"Robot {robot} crashes into robot {grid[r][c][1]}")
          v = False
          break
      if v:
        grid[r][c] = (face, robot)
        locs[robot] = (r, c)
    
    elif atype == "L":
      #print("BEFORE", face, grid[r][c])
      face = (face - num) % 4
      grid[r][c] = (face, robot)
      #print("HERE", face, grid[r][c])

    
    else:
      face = (face + num) % 4
      grid[r][c] = (face, robot)
  if v:
    print("OK")


for tc in range(int(input())):
  solve()
