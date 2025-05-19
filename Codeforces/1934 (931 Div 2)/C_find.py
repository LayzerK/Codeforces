import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  rows, cols = multiple_ints()
  
  print("? 1 1")
  sys.stdout.flush()
  dist1 = int(input())
  #this dist gives the diagonal, bottom left of the diagonal is dist, 1 for (row, col) if dist <= rows-1, otherwise it is moving along the bottom right
  if dist1 <= rows - 1:
    bottom_row = dist1 + 1
    bottom_col = 1
  else:
    bottom_row = rows
    bottom_col = 2 + dist1-rows
  print("? ", bottom_row, bottom_col)
  sys.stdout.flush()
  from_bottom = int(input())
  #this is the dist from the bot left to something
  #now check from t he top right of the diagonal
  if dist1 <= cols-1:
    top_row = 1
    top_col = dist1 + 1
  else:
    top_col = cols
    top_row = 2 + dist1-cols
  
  print("? ", top_row, top_col)
  sys.stdout.flush()
  from_top = int(input())
  
  bot_ans_row = bottom_row-from_bottom//2
  bot_ans_col = bottom_col + from_bottom//2
  #one of these two has to be the mine?
  print("? ",bot_ans_row, bot_ans_col)
  sys.stdout.flush()
  ans_dist = int(input())
  if ans_dist == 0:
    print("! ", bot_ans_row, bot_ans_col)
    sys.stdout.flush()

  else:
    top_ans_row = top_row + from_top//2
    top_ans_col = top_col - from_top//2
    print("! ", top_ans_row, top_ans_col)
    sys.stdout.flush()

  
  
  


for tc in range(int(input())):
  solve()
    