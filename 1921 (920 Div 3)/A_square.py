import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  sides = [tuple(multiple_ints()) for side in range(4)]
  x1,y1 = sides[0]
  for x2,y2 in sides[1:]:
    if y2 == y1:
      print((x1-x2)**2)
      return

for tc in range(int(input())):
  solve()
    