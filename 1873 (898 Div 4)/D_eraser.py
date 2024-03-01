import sys
input = sys.stdin.readline

def solve():
  n,k = map(int, input().strip().split())
  s = input()

  clear = -1
  cost = 0
  for i,val in enumerate(s):
    if val == "B" and i > clear:
      cost += 1
      clear = i + k - 1
  
  print(cost)


for tc in range(int(input())):
  solve()