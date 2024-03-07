import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  start = input().strip()
  goal = input().strip()
  
  bad_cat = 0
  missing_cat = 0
  
  for a,b in zip(start, goal):
    if a == b:
      continue
    if a == "1":
      bad_cat += 1
    else:
      missing_cat += 1
  
  print(max(bad_cat, missing_cat))
    
      

for tc in range(int(input())):
  solve()
    