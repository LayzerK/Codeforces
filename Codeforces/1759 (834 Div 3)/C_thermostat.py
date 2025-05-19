import sys
from math import floor, ceil
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  l,r, minchange = multiple_ints()
  
  start, goal = multiple_ints()
  diff = abs(goal-start)
  if start == goal:
    print(0)  
  elif abs(goal-start) >= minchange:
    print(1)
  else:
    l_delta = start-l
    r_delta = r-start

    l_spare = goal-l
    r_spare = r-goal

    if (l_spare < minchange and r_spare < minchange) or (l_delta < minchange and r_delta < minchange):
      print(-1)    
    elif (l_delta >= minchange and l_spare >= minchange) or (r_delta >= minchange and r_spare >= minchange):
      print(2)
    else:
      print(3)

for tc in range(int(input())):
  solve()
    